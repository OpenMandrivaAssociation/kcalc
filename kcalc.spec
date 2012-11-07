Name:		kcalc
Summary:	Do scientific calculations
Version: 4.9.3
Release: 1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kcalc/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	gmp-devel

%description
KCalc is a calculator which offers many more mathematical functions
than meet the eye on a first glance. Please study the section on
keyboard accelerators and modes in the handbook to learn more about
the many functions available.

%files
%{_kde_appsdir}/kcalc
%{_kde_appsdir}/kconf_update
%{_kde_bindir}/kcalc
%{_kde_applicationsdir}/kcalc.desktop
%{_kde_datadir}/config.kcfg/kcalc.kcfg
%{_kde_docdir}/HTML/*/kcalc
%{_kde_libdir}/libkdeinit4_kcalc.so

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

