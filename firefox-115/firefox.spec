# Private/bundled libs the final package should not provide or depend on.
%global privlibs             libgkcodecs
%global privlibs %{privlibs}|liblgpllibs
%global privlibs %{privlibs}|libmozavcodec
%global privlibs %{privlibs}|libmozavutil
%global privlibs %{privlibs}|libmozgtk
%global privlibs %{privlibs}|libmozsandbox
%global privlibs %{privlibs}|libmozsqlite3
%global privlibs %{privlibs}|libmozwayland
%global privlibs %{privlibs}|libxul

%global __provides_exclude ^(%{privlibs})\\.so
%global __requires_exclude ^(%{privlibs})\\.so

Name:		firefox
Version:	115.9.1
Release:	1%{?dist}
Summary:	Mozilla Firefox

License:	MPLv2.0
URL:		https://www.firefox.com/
Source0:	%{name}-%{version}.tar.bz2
Patch1:		0001-Patch-glslopt-to-build-with-host-compiler.patch
Patch2:		0002-Reduce-Rust-build-memory-requirements.patch
Patch3:		0003-Skip-libclang-version-check.patch
#Patch4:		0004-Disable-devtools-in-browser.patch

BuildRequires:	rust
BuildRequires:	rust-std-static
BuildRequires:	cargo
BuildRequires:	cbindgen >= 0.27.0
BuildRequires:	clang-devel
BuildRequires:	llvm
BuildRequires:	python3-base
BuildRequires:	python3-curses
BuildRequires:	python3-devel
BuildRequires:	zip
BuildRequires:	unzip

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:	pkgconfig(nspr) >= 4.36.0
BuildRequires: 	pkgconfig(nss) >= 3.110.0

%description
Mozilla Firefox web browser

%define build_dir $PWD/..

%prep
%autosetup -p1 -n %{name}-%{version}

%ifarch %arm32
%define SB2_TARGET armv7-unknown-linux-gnueabihf
echo "Target is %SB2_TARGET"
%endif
%ifarch %arm64
%define SB2_TARGET aarch64-unknown-linux-gnu
echo "Target is %SB2_TARGET"
%endif
%ifarch %ix86
%define SB2_TARGET i686-unknown-linux-gnu
echo "Target is %SB2_TARGET"
%endif

echo "Target is %SB2_TARGET"

cat > "%{build_dir}"/rpm-shared.env <<EOF
export MOZCONFIG='%{build_dir}/mozconfig'
export LIBDIR='%{_libdir}'
export MOZ_OBJDIR='%{build_dir}/obj'
export CARGO_HOME='%{build_dir}/cargo'
export MOZBUILD_STATE_PATH='%{build_dir}'
export MACH_BUILD_PYTHON_NATIVE_PACKAGE_SOURCE=system

# When cross-compiling under SB2 rust needs to know what arch to emit
# when nothing is specified on the command line. That usually defaults
# to "whatever rust was built as" but in SB2 rust is accelerated and
# would produce x86 so this is how it knows differently. Not needed
# for native x86 builds
export SB2_RUST_TARGET_TRIPLE=%SB2_TARGET

export RUST_TARGET=%SB2_TARGET
export TARGET=%SB2_TARGET
export HOST=%SB2_TARGET
export SB2_TARGET=%SB2_TARGET

export CC=gcc
export CXX=g++
export AR="gcc-ar"
export NM="gcc-nm"
export RANLIB="gcc-ranlib"

# llvm tool used by default would use too much memory
export READELF=readelf

export CARGOFLAGS=" --offline"
export CARGO_NET_OFFLINE=1
export CARGO_BUILD_TARGET=armv7-unknown-linux-gnueabihf
export CARGO_CFG_TARGET_ARCH=arm
EOF

%build
source "%{build_dir}"/rpm-shared.env

# Expose the elf32-i386 libclang.so for use inside the arm target, JB#55042
mkdir -p "%{build_dir}"/lib
SBOX_DISABLE_MAPPING=1 find /usr/lib -maxdepth 1 -name 'libclang.so.*' -exec cp {} "%{build_dir}"/lib/ \;

cat > "$MOZCONFIG" <<EOF
mk_add_options MOZ_OBJDIR='%{build_dir}/obj'

%ifarch %arm32 %arm64
# Garbage collect on arm to reduce memory requirements, JB#55074
FIX_LDFLAGS="-Wl,--gc-sections -Wl,--reduce-memory-overheads -Wl,--no-keep-memory"
%else
FIX_LDFLAGS="-Wl,--reduce-memory-overheads -Wl,--no-keep-memory"
%endif
export LDFLAGS="\$FIX_LDFLAGS"
export WRAP_LDFLAGS="\$FIX_LDFLAGS"
mk_add_options LDFLAGS="\$FIX_LDFLAGS"

. \$topsrcdir/browser/config/mozconfig

ac_add_options --disable-bootstrap
ac_add_options --prefix=%{_prefix}
ac_add_options --libdir=%{_libdir}
ac_add_options --includedir=%{_includedir}
ac_add_options --enable-release
ac_add_options --disable-updater
ac_add_options --disable-crashreporter
ac_add_options --disable-tests
ac_add_options --enable-default-toolkit=cairo-gtk3-wayland
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-libclang-path='%{build_dir}/lib/'
ac_add_options --disable-nodejs
ac_add_options --without-wasm-sandboxed-libraries

%ifarch %ix86
ac_add_options --disable-startupcache
ac_add_options --host=i686-unknown-linux-gnu
%endif

%ifarch %arm32
ac_add_options --host=armv7-unknown-linux-gnueabihf
%endif

%ifarch %arm64
ac_add_options --host=aarch64-unknown-linux-gnu

%endif
EOF

export CFLAGS="$(echo " %{optflags} " | sed 's/ -fexceptions / /g')"
export CXXFLAGS="$(echo " %{optflags} " | sed 's/ -fexceptions / /g')"

./mach build

%install
%{__make} -C "%{build_dir}"/obj/browser/installer install STRIP=/bin/true DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/firefox/firefox-bin
rm -f %{buildroot}%{_libdir}/firefox/removed-files

%files
%{_bindir}/firefox
%{_libdir}/firefox/

%changelog

