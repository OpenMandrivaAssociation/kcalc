Name:		kcalc
Summary:	Do scientific calculations
Version:	20.08.1
Release:	2
Group:		Graphical desktop/KDE
License:	LGPLv2
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
URL:		http://utils.kde.org/projects/kcalc/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		kcalc-19.04.1-menuentry.patch
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Init)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel

%description
KCalc is a calculator which offers many more mathematical functions
than meet the eye on a first glance. Please study the section on
keyboard accelerators and modes in the handbook to learn more about
the many functions available.

%files -f %{name}.lang
%{_bindir}/kcalc
%{_libdir}/libkdeinit5_kcalc.so
%{_datadir}/applications/org.kde.kcalc.desktop
%{_datadir}/config.kcfg/kcalc.kcfg
%{_datadir}/kcalc/scienceconstants.xml
%{_datadir}/kconf_update/kcalcrc.upd
%{_datadir}/kxmlgui5/kcalc/kcalcui.rc
%{_datadir}/metainfo/org.kde.kcalc.appdata.xml

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
