%define bootstrap 0
%{?_without_bootstrap: %global bootstrap 0}
%{?_with_bootstrap: %global bootstrap 1}

# mklibname should handle the special cases of library naming
%define major 6
%define develname %mklibname -d x11

%define xcbmajor 1

%define subrel 1

Name: libx11
Summary: X Library
Version: 1.8.6
Release: 1
Group: System/Libraries
License: MIT
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/lib/libX11-%{version}.tar.xz
Provides: libxorg-x11
Patch0: libX11-1.3.5-fix-null-pointer.patch
Patch1: libx11-fix-segfault.diff
# (tv) fix bug #7797 (lack of support for mn_MN locale):
Patch2: libx11-add_mn_locale.diff
#
# CVE-2023-43785 (fix)
# https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/6858d468d9ca55fb4c5fd70b223dbc78a3358a7f
Patch3: 6858d468d9ca55fb4c5fd70b223dbc78a3358a7f.patch
#
# CVE-2023-43786 (fix)
# https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/204c3393c4c90a29ed6bef64e43849536e863a86
Patch4: 204c3393c4c90a29ed6bef64e43849536e863a86.patch
# CVE-2023-43786 (hardening)
# https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/73a37d5f2fcadd6540159b432a70d80f442ddf4a
Patch5: 73a37d5f2fcadd6540159b432a70d80f442ddf4a.patch
# https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/b4031fc023816aca07fbd592ed97010b9b48784b
Patch6: b4031fc023816aca07fbd592ed97010b9b48784b.patch
#
# CVE-2023-43787 (fix)
# https://gitlab.freedesktop.org/xorg/lib/libx11/-/commit/7916869d16bdd115ac5be30a67c3749907aea6a0
Patch7: 7916869d16bdd115ac5be30a67c3749907aea6a0.patch

BuildRequires: x11-util-macros		>= 1.1.5
BuildRequires: pkgconfig(xtrans)		>= 1.0.4
BuildRequires: pkgconfig(xdmcp)		>= 1.0.2
BuildRequires: pkgconfig(xau)		>= 1.0.3
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: pkgconfig(xcb)
%if !%{bootstrap}
BuildRequires: groff			> 1.19.1
BuildRequires: xmlto
%endif
BuildRequires: x11-sgml-doctools
BuildRequires: docbook-style-xsl

# because of %%{_datadir/X11} being owned by x11-server-common
#Requires(pre): x11-server-common >= 1.4.0.90-13mdv #mpol, needed?

Provides: %{name} = %{version}
Requires(post): grep
Requires(postun): grep coreutils

%description
%{name} contains the shared libraries that most X programs
need to run properly. These shared libraries are in a separate package in
order to reduce the disk space needed to run X applications on a machine
without an X server (i.e, over a network).

#-----------------------------------------------------------

%files -n libx11
%{_libdir}/libX11.so.%{major}
%{_libdir}/libX11.so.%{major}.*

%post -n libx11
if  grep -q "^%{_prefix}/X11R6/lib$" /etc/ld.so.conf; then
    grep -v "^%{_prefix}/X11R6/lib$" /etc/ld.so.conf > /etc/ld.so.conf.new
    mv -f /etc/ld.so.conf.new /etc/ld.so.conf
    /sbin/ldconfig
fi

%postun -n libx11
if [ "$1" = "0" \
   -a "`grep "^%{_prefix}/X11R6/lib$" /etc/ld.so.conf`" != "" ]; then
    grep -v "^%{_prefix}/X11R6/lib$" /etc/ld.so.conf > /etc/ld.so.conf.new
    mv -f /etc/ld.so.conf.new /etc/ld.so.conf
    /sbin/ldconfig
fi

#-----------------------------------------------------------

%package -n libx11-xcb
Summary: X Library
Group: Development/X11
Provides: %{name}-xcb = %{version}
Conflicts: %{_lib}x11_6 < 1.6.1-2

%description -n libx11-xcb
%{name}-xcb contains the shared libraries that most X programs
need to run properly. These shared libraries are in a separate package in
order to reduce the disk space needed to run X applications on a machine
without an X server (i.e, over a network).

%files -n libx11-xcb
%{_libdir}/libX11-xcb.so.*

#-----------------------------------------------------------

%package -n libx11-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: libx11 = %{version}-%{release}
Requires: libx11-xcb = %{version}-%{release}
Provides: libx11-devel = %{version}-%{release}
Provides: libx11-xcb-devel = %{version}-%{release}
Conflicts: x11-proto-devel < 2019.2-2

%description -n libx11-devel
%{name} includes the libraries and header files you'll need to develop
programs which run in X clients. X11 includes the base Xlib library as
well as the Xt and Xaw widget sets.

Install %{name} if you are going to develop programs which
will run as X clients.

%files -n libx11-devel
%{_mandir}/man3/*.3.*
%{_libdir}/libX11.so
%{_libdir}/pkgconfig/x11.pc
%{_includedir}/X11/cursorfont.h
%{_includedir}/X11/ImUtil.h
%{_includedir}/X11/Xlocale.h
%{_includedir}/X11/Xcms.h
%{_includedir}/X11/Xlibint.h
%{_includedir}/X11/Xlib.h
%{_includedir}/X11/Xresource.h
%{_includedir}/X11/Xregion.h
%{_includedir}/X11/Xutil.h
%{_includedir}/X11/XlibConf.h
%{_includedir}/X11/XKBlib.h
%{_includedir}/X11/extensions/XKBgeom.h
%{_libdir}/libX11-xcb.so
%{_libdir}/pkgconfig/x11-xcb.pc
%{_includedir}/X11/Xlib-xcb.h
%{_mandir}/man5/*.5*

#-----------------------------------------------------------

%package common
Summary: Common files used by the X.org
Group: System/X11

%description common
Common files used by the X.org

%files common
%dir %{_datadir}/X11/locale
%{_datadir}/X11/locale/*
%{_datadir}/X11/Xcms.txt
%{_datadir}/X11/XErrorDB

#-----------------------------------------------------------

%package doc
Summary: Documentation for %{name}
Group: Documentation
BuildArch: noarch
Conflicts: libx11-devel < 1.4.99.1-3.mga2

%description doc
This package includes the documentation for the base Xlib library.

For guidance on programming with these libraries, O'Reilly & Associates
produces a series on X programming which you might find useful.

%files doc
%dir %{_docdir}/libX11
%{_docdir}/libX11/*

#-----------------------------------------------------------

%prep
%autosetup -p1 -n libX11-%{version}

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete

