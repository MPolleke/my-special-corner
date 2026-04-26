%define bootstrap 0
%{?_without_bootstrap: %global bootstrap 0}
%{?_with_bootstrap: %global bootstrap 1}

Name: libxcb
Summary: X protocol C-language Binding Library
Version: 1.15
Release: 2
Group: System/X11
License: MIT
URL: https://xcb.freedesktop.org
Source0: https://xcb.freedesktop.org/dist/libxcb-%{version}.tar.xz

BuildRequires:  pkgconfig(xcb-proto) >= 1.13

BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libpthread-stubs
BuildRequires: libxslt-proc
BuildRequires: pkgconfig(xdmcp)
BuildRequires: pkgconfig(xau)
BuildRequires: python3-devel
%if !%bootstrap
BuildRequires: doxygen
BuildRequires: graphviz
%endif

%description
the X protocol C-language Binding (XCB) is a replacement for Xlib  featuring
a small footprint, latency hiding, direct access to the protocol, improved
threading support, and extensibility.

%files -n libxcb
%{_libdir}/libxcb.so.*
%{_libdir}/libxcb-*.so.*

#-----------------------------------------------------------

%package -n libxcb-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: x11-proto-devel >= 1.2.0
Provides: xcb-devel = %{version}-%{release}
Provides: libxcb-devel = %{version}-%{release}

Requires: libxcb = %{version}

# gw this isn't picked up by the automatic pkgconfig deps, but without it,
# pkg-config --libs xcb will fail
Requires: libpthread-stubs

%description -n libxcb-devel
Development files for %{name}.

%files -n libxcb-devel
%dir %{_includedir}/xcb
%{_includedir}/xcb/*.h
%{_libdir}/libxcb*.so
%{_libdir}/pkgconfig/xcb*.pc
%{_mandir}/*/*

#-----------------------------------------------------------

%package doc
Summary: Documentation for %{name}
Group: Development/X11

%description doc
Documentation for %{name}.

%files doc
%{_docdir}/libxcb

#-----------------------------------------------------------

%prep
%setup -q
%autosetup -p1

%build
%configure --disable-static

%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete
