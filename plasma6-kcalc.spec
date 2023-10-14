%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define git 20231015

Name:		plasma6-kcalc
Summary:	Do scientific calculations
Version:	23.07.90
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	LGPLv2
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
URL:		http://utils.kde.org/projects/kcalc/
%if 0%{?git:1}
Source0:	https://invent.kde.org/utilities/kcalc/-/archive/master/kcalc-master.tar.bz2#/kcalc-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%endif

BuildRequires:  cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6ConfigWidgets)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6GuiAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	gmp-devel
BuildRequires:	mpfr-devel

%description
KCalc is a calculator which offers many more mathematical functions
than meet the eye on a first glance. Please study the section on
keyboard accelerators and modes in the handbook to learn more about
the many functions available.

%files -f kcalc.lang
%{_bindir}/kcalc
%{_datadir}/applications/org.kde.kcalc.desktop
%{_datadir}/config.kcfg/kcalc.kcfg
%{_datadir}/kconf_update/kcalcrc.upd
%{_datadir}/metainfo/org.kde.kcalc.appdata.xml
%{_datadir}/kglobalaccel/org.kde.kcalc.desktop

#----------------------------------------------------------------------

%prep
%autosetup -n kcalc-%{?git:master}%{!?git:%{version}} -p1
%cmake  \
          -DBUILD_WITH_QT6:BOOL=ON \
          -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kcalc --with-html
