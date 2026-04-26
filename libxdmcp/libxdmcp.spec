%define major 6

Name: libxdmcp
Summary: X Display Manager Control Protocol library
Version: 1.1.4
Release: 1
Group: Development/X11
License: MIT
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.xz
Provides: %{name} = %{version}

BuildRequires: pkgconfig(libbsd)
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Display Manager Control Protocol library

#-----------------------------------------------------------

%files -n libxdmcp
%{_libdir}/libXdmcp.so.*

#-----------------------------------------------------------

%package -n libxdmcp-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: libxdmcp = %{version}-%{release}
Provides: libxdmcp-devel = %{version}-%{release}

%description -n libxdmcp-devel
Development files for %{name}

%files -n libxdmcp-devel
%{_datadir}/doc/libXdmcp/xdmcp.xml
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.pc
%{_includedir}/X11/Xdmcp.h

%prep
%setup -q -n libXdmcp-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} \
		--without-xmlto \
		--disable-static

%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete

