Name:		kcalc
Summary:	Do scientific calculations
Version:	15.04.2
Release:	1
Group:		Graphical desktop/KDE
License:	LGPLv2
URL:		http://utils.kde.org/projects/kcalc/
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5XmlGui)
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
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
