%define major 6
%define libxau %mklibname xau %{major}
%define devxau %mklibname xau -d

Name: libxau
Summary: X authorization file management library
Version: 1.0.11
Release: 1
Group: Development/X11
License: MIT
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/lib/libXau-%{version}.tar.xz
Provides: %{name} = %{version}

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X authorization file management library

%files -n libxau
%{_libdir}/libXau.so.%{major}
%{_libdir}/libXau.so.%{major}.*

#-----------------------------------------------------------

%package -n libxau-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: libxau = %{version}-%{release}
Provides: libxau-devel = %{version}-%{release}
Obsoletes: %{_lib}xau6-devel < 1.0.8-2
Obsoletes: %{_lib}xau6-static-devel < 1.0.8-2

%description -n libxau-devel
Development files for %{name}

%pre -n libxau-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n libxau-devel
%{_libdir}/pkgconfig/xau.pc
%{_includedir}/X11/Xauth.h
%{_libdir}/libXau.so
%{_mandir}/man3/Xau*

#-----------------------------------------------------------

%prep
%setup -q -n libXau-%{version}

%autopatch -p1

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} \
		--disable-static

%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete

