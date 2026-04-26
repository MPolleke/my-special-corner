%define major	6
%define libname %mklibname ice %{major}
%define devname	%mklibname ice -d

Name:		libice
Summary:	X Inter Client Exchange Library
Version:	1.1.1
Release:	1
Group:		Development/X11
License:	MIT
URL:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libICE-%{version}.tar.xz

BuildRequires:	pkgconfig(libbsd)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(xtrans) >= 1.0.0

%description
libice provides an interface to ICE, the Inter-Client Exchange protocol.
Motivated by issues arising from the need for X Window System clients to
share data with each other, the ICE protocol provides a generic framework for
building protocols on top of reliable, byte-stream transport connections. It
provides basic mechanisms for setting up and shutting down connections, for
performing authentication, for negotiating versions, and for reporting
errors.


%package -n	libice-devel
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	libice = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n libice-devel
Development files for %{name}

#-----------------------------------------------------------

%prep
%setup -q -n libICE-%{version}

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir} \
	--disable-static

%make_build

%install
%make_install

mv %{buildroot}%{_defaultdocdir}/libICE installed-docs

#we don't want these
find %{buildroot} -name "*.la" -delete

%files -n libice-devel
%doc installed-docs/*
%{_libdir}/libICE.so
%{_libdir}/pkgconfig/ice.pc
%{_includedir}/X11/ICE/ICEutil.h
%{_includedir}/X11/ICE/ICE.h
%{_includedir}/X11/ICE/ICEproto.h
%{_includedir}/X11/ICE/ICEconn.h
%{_includedir}/X11/ICE/ICElib.h
%{_includedir}/X11/ICE/ICEmsg.h

%files -n libice
%{_libdir}/libICE.so.*
