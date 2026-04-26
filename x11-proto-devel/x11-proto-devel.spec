%define bootstrap 0
%{?_without_bootstrap: %global bootstrap 0}
%{?_with_bootstrap: %global bootstrap 1}

%define vnc_version 1.0.0
%define xcb_version 1.15.2

Name: x11-proto-devel
Summary: Xorg X11 protocol specification headers
Version: 2022.2
Release: 2
Group: Development/X11
License: MIT
URL: https://xorg.freedesktop.org
BuildArch: noarch
Source0: https://xorg.freedesktop.org/archive/individual/proto/xorgproto-%{version}.tar.xz
# FIXME: to be split:
Source31: http://xf4vnc.sf.net/vncproto-%{vnc_version}.tar.bz2
Source32: https://xorg.freedesktop.org/archive/individual/proto/xcb-proto-%{xcb_version}.tar.xz

BuildRequires: meson >= 0.43
BuildRequires: x11-util-macros >= 1.0.1

%if !%{bootstrap}
# For docs:
BuildRequires: docbook-dtd412-xml
BuildRequires: docbook-dtd45-xml
BuildRequires: docbook-style-xsl
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: x11-sgml-doctools
%endif

BuildRequires: python3-base

%description
X.Org X11 Protocol headers

#-----------------------------------------------------------

%package -n x11-proto-doc

Summary: Documentation for the X11 protocol and extensions
Group:   Development/X11
BuildArch:	noarch

%description -n x11-proto-doc
Documentation for the X11 protocol and extensions.

#-----------------------------------------------------------

%prep
%setup -q -n xorgproto-%version -a31 -a32

%build
%meson -Dlegacy=true
%meson_build

# vncproto is from cvs
pushd vncproto-*
aclocal
automake -a -c
autoconf
popd

for dir in vnc*/ xcb*/; do
pushd $dir
sed -i -e 's,^\(pkgconfigdir =\).*,\1 ${datadir}/pkgconfig,' Makefile.am
autoreconf -vfi
%configure --without-fop --build=%{_build}
%make_build
popd
done

%install
%meson_install
for dir in vnc*/ xcb*/; do
    if [ -d $dir ]; then
	pushd $dir
	%make_install
	popd
    fi
done

# refer to https://gitlab.freedesktop.org/xorg/proto/xorgproto/issues/10
# These headers refer to libX11 types and don't belong in this package.
# libX11 and libXvMC have been updated to supply these headers themselves
# now, so these are only useful for building older versions of those libraries.
# So let's drop conflicting files (mga#26176) as we build with "legacy" turned on:

# now in libx11 since release 1.6.9
rm -rf %{buildroot}%{_includedir}/X11/extensions/XKBgeom.h
# now in libXvMC since release 1.0.12
rm -rf %{buildroot}%{_includedir}/X11/extensions/vldXvMC.h

rm -rf %{buildroot}%{_datadir}/doc/xorgproto/*.txt
rm -rf %{buildroot}%{_datadir}/doc/xorgproto/PM_spec

%files
%dir %{_datadir}/xcb
%{_includedir}/GL/glx*
%{_includedir}/GL/internal/*
%{_includedir}/X11/*.h
%{_includedir}/X11/dri/*
%{_includedir}/X11/extensions/*
%{_includedir}/X11/fonts/*
%{_includedir}/X11/PM/*
%{_datadir}/pkgconfig/*.pc
%{_datadir}/xcb/*
# xcbgen stuff
%{python3_sitelib}/xcbgen/

%files -n x11-proto-doc
%doc *.txt PM_spec

