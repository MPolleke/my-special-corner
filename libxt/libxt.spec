%define major 6
%define libxt %mklibname xt %major
%define libxt_devel %mklibname xt -d

Name: libxt
Summary: X Toolkit Intrinsics library
Version: 1.2.1
Release: 2
Group: Development/X11
License: MIT
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/lib/libXt-%{version}.tar.bz2
BuildRequires: pkgconfig(sm) >= 1.0.0
BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Provides: %{name} = %{version}

%description
X Toolkit Intrinsics library used to build older generation toolkits such
as Motif & Xaw.

%files -n libxt
%{_libdir}/libXt.so.%{major}{,.*}

#-----------------------------------------------------------

%package -n libxt_devel
Summary: Development files for %{name}
Group: Development/X11
Requires: libxt = %{version}-%{release}
Provides: libxt-devel = %{version}-%{release}
Obsoletes: %{_lib}xt-static-devel < 1.1.4-2

%description -n libxt_devel
Development files for %{name}.

%files -n libxt_devel
%{_libdir}/libXt.so
%{_libdir}/pkgconfig/xt.pc
%{_includedir}/X11/Core.h
%{_includedir}/X11/VarargsI.h
%{_includedir}/X11/RectObj.h
%{_includedir}/X11/TranslateI.h
%{_includedir}/X11/Vendor.h
%{_includedir}/X11/CallbackI.h
%{_includedir}/X11/ResConfigP.h
%{_includedir}/X11/IntrinsicI.h
%{_includedir}/X11/IntrinsicP.h
%{_includedir}/X11/ConstrainP.h
%{_includedir}/X11/Constraint.h
%{_includedir}/X11/InitialI.h
%{_includedir}/X11/EventI.h
%{_includedir}/X11/ObjectP.h
%{_includedir}/X11/Xtos.h
%{_includedir}/X11/CreateI.h
%{_includedir}/X11/Intrinsic.h
%{_includedir}/X11/CoreP.h
%{_includedir}/X11/Object.h
%{_includedir}/X11/CompositeP.h
%{_includedir}/X11/HookObjI.h
%{_includedir}/X11/RectObjP.h
%{_includedir}/X11/ConvertI.h
%{_includedir}/X11/Shell.h
%{_includedir}/X11/ShellI.h
%{_includedir}/X11/ShellP.h
%{_includedir}/X11/StringDefs.h
%{_includedir}/X11/VendorP.h
%{_includedir}/X11/SelectionI.h
%{_includedir}/X11/PassivGraI.h
%{_includedir}/X11/Composite.h
%{_includedir}/X11/ThreadsI.h
%{_includedir}/X11/ResourceI.h
%{_mandir}/man3/Xt*.3*
%{_mandir}/man3/Menu*
%{_datadir}/doc/libXt/*

#-----------------------------------------------------------

%prep
%setup -q -n libXt-%{version}
%autopatch -p1

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} \
		--disable-static

%make_build

%install
%make_install

#we don't want these
find %{buildroot} -name "*.la" -delete

