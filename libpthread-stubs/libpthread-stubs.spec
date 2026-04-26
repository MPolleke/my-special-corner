# This package only contains arch specific .pc file
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Name: libpthread-stubs
Summary: PThread Stubs for XCB
Version: 0.4
Release: 4
Group: System/X11
License: MIT
URL: https://xcb.freedesktop.org
Source0: https://xcb.freedesktop.org/dist/libpthread-stubs-%{version}.tar.bz2
BuildRequires: x11-proto-devel >= 1.2.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: libxslt-proc

%description
PThread Stubs for XCB

%prep
%setup -q -n libpthread-stubs-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%{_libdir}/pkgconfig/pthread-stubs.pc
