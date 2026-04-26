Name: xtrans
Summary:  Abstract network code for X
Version: 1.4.0
Release: 3
Group: Development/X11
BuildArch: noarch
License: MIT
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/lib/xtrans-%{version}.tar.bz2

%description
Abstract network code for X

%prep
%setup -q -n xtrans-%{version}

%build
%configure --build=%{_build}
%make_build

%install
%make_install
rm %{buildroot}%{_datadir}/doc/xtrans/xtrans.*

%files
%doc doc/xtrans.xml
%{_datadir}/pkgconfig/xtrans.pc
%{_datadir}/aclocal/xtrans.m4
%{_includedir}/X11/Xtrans/Xtransint.h
%{_includedir}/X11/Xtrans/Xtrans.h
%{_includedir}/X11/Xtrans/Xtrans.c
%{_includedir}/X11/Xtrans/Xtranslcl.c
%{_includedir}/X11/Xtrans/Xtranssock.c
%{_includedir}/X11/Xtrans/Xtransutil.c
%{_includedir}/X11/Xtrans/transport.c

