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
Version:	115.37.0
Release:	1%{?dist}
Summary:	Mozilla Firefox

License:	MPLv2.0
URL:		https://www.firefox.com/
Source0:	%{name}-%{version}.tar.bz2
Patch1:     0001-Add-symlink-to-embedlite.-JB-52893.patch
Patch2:     0002-Bring-back-Qt-layer.-JB-50505.patch
Patch3:     0003-Fix-embedlite-building.-JB-50505.patch
Patch4:     0004-Read-rustc-host-from-environment.-JB-53019-OMP-JOLLA.patch
Patch5:     0005-Provide-checkbox-radio-renderer-for-Sailfish-OS.-Con.patch
Patch6:     0006-Fix-GLContextProvider-defines.patch
Patch7:     0007-Whitelist-sync-messages-of-EmbedLite.-JB-50505.patch
Patch8:     0008-Cleanup-static-components-definitions.-JB-55835-OMP-.patch
Patch9:     0009-Reduce-Rust-build-requirements.patch
Patch10:     0010-Patch-glslopt-to-build-on-arm.patch
Patch11:     0011-Disable-MOC-code-generation-for-message_pump_qt.patch
Patch12:     0012-Backport-Embed-MessageLoop-contructor-back-sha1-eb2d.patch
Patch13:     0013-Allow-compositor-specializations-to-override-the-com.patch
Patch14:     0014-Revert-Bug-1676576-Remove-unused-functions-of-Compos.patch
Patch15:     0015-Hackish-fix-for-preferences-usage-in-Parent-process-.patch
Patch16:     0016-Revert-Bug-1706051-Remove-some-IPC-messages-that-are.patch
Patch17:     0017-Revert-Bug-1494175-Remove-unimplemented-nsIWebBrowse.patch
Patch18:     0018-Fix-embedlite-building.-JB-50505.patch
Patch19:     0019-Revert-Bug-1567888-remove-unneeded-QT-related-rules-.patch
Patch20:     0020-Allow-gen_last_modified.py-to-complete.patch
Patch21:     0021-Force-to-build-mozglue-and-xpcomglue-static-librarie.patch
Patch22:     0022-Revert-Bug-445128-Stop-putting-the-version-number-in.patch
Patch23:     0023-Revert-Bug-1427455-Remove-unused-variables-from-base.patch
Patch24:     0024-Revert-Bug-1333826-Remove-SDK_FILES-SDK_LIBRARY-and-.patch
Patch25:     0025-Revert-Bug-1333826-Remove-the-make-sdk-build-target-.patch
Patch26:     0026-Revert-Bug-1333826-Remove-a-few-references-from-.mk-.patch
Patch27:     0027-Introduce-EmbedInitGlue-to-the-mozglue.-JB-50788.patch
Patch28:     0028-Split-namespace-into-two-blocks.patch
Patch29:     0029-Do-not-create-CreateFallbackSurface.-JB-55226-OMP-JO.patch
Patch30:     0030-Make-PresShell-SetIsActive-public.patch
Patch31:     0031-Drop-swap_buffers_with_damage-extension-support.-Fix.patch
Patch32:     0032-Add-patch-to-fix-32-bit-builds.patch
Patch33:     0033-Fix-gfxPlatform-AsyncPanZoomEnabled-for-embedlite.-J.patch
Patch34:     0034-Supress-URLQueryStrippingListService.jsm-error.patch
Patch35:     0035-Allow-file-scheme-when-loading-OpenSearch-providers.patch
Patch36:     0036-Add-and-adjust-embedlite-static-prefs.patch
Patch37:     0037-Disable-SessionStore-functionality.patch
Patch38:     0038-Prevent-errors-from-DownloadPrompter.patch
Patch39:     0039-Restore-NotifyDidPaint-event-and-timers.patch
Patch40:     0040-Adapt-build-configuration-for-SailfishOS.-JB-53756.patch
Patch41:     0041-Update-GN-build-files-for-WebRTC.-JB-53756.patch
Patch42:     0042-Disable-desktop-sharing-feature-on-SFOS.-JB-53756.patch
Patch43:     0043-Implement-video-capture-module.-JB-53982.patch
Patch44:     0044-Regenerate-moz.build-files.-JB-53756.patch
Patch45:     0045-Drop-AudioPlayback-messages-if-no-embedder-element-i.patch
Patch46:     0046-Get-ContentFrameMessageManager-via-nsIDocShellTreeOw.patch
Patch47:     0047-Convert-panic-into-early-return-in-Hyphenator.patch
Patch48:     0048-Allow-LoginManagerPrompter-to-find-its-window.-JB-55.patch
Patch49:     0049-Add-support-for-prefers-color-scheme-JB-58394.patch
Patch50:     0050-Update-hash-for-mapped_hyph.patch
Patch51:     0051-Fix-content-action-integration-to-work.-Fixes-JB-512.patch
Patch52:     0052-Make-fullscreen-enabling-work-as-used-to-with-pref-f.patch
Patch53:     0053-Force-use-of-mobile-video-controls.-JB-55484-OMP-JOL.patch
Patch54:     0054-Add-a-video-decoder-based-on-gecko-camera.-JB-56755.patch
Patch55:     0055-Fix-audio-underruns-for-fullduplex-mode.-JB-55461.patch
Patch56:     0056-Ensure-audio-continues-when-screen-is-locked.-Contri.patch
Patch57:     0057-Delete-startupCache-if-it-s-stale.patch
Patch58:     0058-Hardcode-loopback-address-for-profile-lock-filename..patch
Patch59:     0059-Start-using-user-agent-builder.-JB-52068.patch
Patch60:     0060-Disallow-page-zooming-if-the-meta-viewport-scale-is-.patch
Patch61:     0061-Add-preference-to-bypass-CORS-on-nsContentSecurityMa.patch
Patch62:     0062-Get-12-24h-timeformat-setting-from-dconf.-Fixes-JB-5.patch
Patch63:     0063-Bug-1710603-Allow-stat-on-from-socket-process-for-gl.patch
Patch64:     0064-Update-content-signature-root-hash.-JB-63099.patch
Patch65:     0065-Bug-1773259-Work-around-build-failure-with-newer-cbi.patch
Patch66:     0066-Bug-1880013-Update-glslopt-to-0.1.10-for-C-20-fix.-r.patch
Patch67:     0067-Bug-1913645-Update-glslopt-to-0.1.11-to-fix-aarch64-.patch
Patch68:     0068-Bug-1998927-Update-glslopt-to-explicitly-define-MOZI.patch
Patch69:     0069-Bug-1999625-Update-glslopt-to-0.1.13.-r-gfx-reviewer.patch
Patch70:     0070-Bug-2017954-Update-glslopt-to-0.1.14-r-jnicol-gfx-re.patch
Patch71:     0071-Clean-up-Gecko-configure-integration.patch
Patch72:     0072-Adapt-EmbedLite-WebRender-offscreen-compositing.patch
Patch73:     0073-Restore-EmbedLite-native-prompt-dialogs.patch
Patch74:     0074-Guard-media-sink-suspend-before-initialization.patch
Patch75:     0075-Allow-disabling-default-protocol-handler-injection.patch
Patch76:     0076-Fix-EmbedLite-toolkit-error-pages.patch
Patch77:     0077-Use-EmbedLite-helper-app-dialog-static-registration.patch
Patch78:     0078-Load-EmbedLite-search-engines-from-settings.patch
Patch79:     0079-Dispatch-MDSM-initialization-without-tail-dispatch.patch
Patch80:     0080-Preload-autoplay-metadata-before-inaudible-check.patch
Patch81:     0081-Fix-Qt-form-control-theme-rendering.patch
Patch82:     0082-Keep-about-support-snapshot-resilient-in-EmbedLite.patch
Patch83:     0083-Register-gecko-camera-decoder-in-remote-video-paths.patch
Patch84:     0084-Use-system-sqlite.patch


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

%ifarch %arm32_
%define SB2_TARGET armv7-unknown-linux-gnueabihf
echo "Target is %SB2_TARGET"
%endif
#%ifarch %arm64
%define SB2_TARGET aarch64-unknown-linux-gnu
echo "Target is %SB2_TARGET"
#%endif
%ifarch %ix86_
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
export RUST_HOST_TARGET=%SB2_TARGET


%ifarch %arm32 %arm64
# This should be define...
export CROSS_COMPILE=%SB2_TARGET
%endif

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
#ac_add_options --with-libclang-path='%{build_dir}/lib/'
ac_add_options --disable-nodejs
ac_add_options --without-wasm-sandboxed-libraries

%ifarch %ix86
#ac_add_options --disable-startupcache
#ac_add_options --host=i686-unknown-linux-gnu
%endif

%ifarch %arm32
#ac_add_options --host=armv7-unknown-linux-gnueabihf
%endif

%ifarch %arm64
ac_add_options --host=aarch64-unknown-linux-gnu
ac_add_options --target=aarch64-unknown-linux-gnu
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

