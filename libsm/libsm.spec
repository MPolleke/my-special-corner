%define major	6
%define libname %mklibname sm %{major}
%define devname	%mklibname sm -d

Name:		libsm
Summary: 	X Session Management Library
Version:	1.2.4
Release:	1
Group:		Development/X11
License:	MIT
URL:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libSM-%{version}.tar.xz

BuildRequires:	pkgconfig(ice) >= 1.0.0
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(xtrans) >= 1.0.0
BuildRequires:	pkgconfig(uuid)

%description
This is the X Session Management Library.


%package -n	libsm-devel
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	libsm = %{version}-%{release}
Provides:	libsm-devel = %{version}-%{release}
Obsoletes:	libsm6-devel < 1.2.0-3
Conflicts:	libxorg-x11-devel < 7.0

%description -n libsm-devel
Development files for %{name}.

#-----------------------------------------------------------

%prep
%setup -q -n libSM-%{version}

%build
%configure	\
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir} \
	--disable-static

%make_build

%install
%make_install

mv %{buildroot}%{_defaultdocdir}/libSM installed-docs

#we don't want these
find %{buildroot} -name "*.la" -delete

%files -n libsm-devel
%doc installed-docs/*
%{_libdir}/libSM.so
%{_libdir}/pkgconfig/sm.pc
%{_includedir}/X11/SM/SM.h
%{_includedir}/X11/SM/SMlib.h
%{_includedir}/X11/SM/SMproto.h

%files -n libsm
%{_libdir}/libSM.so.*

