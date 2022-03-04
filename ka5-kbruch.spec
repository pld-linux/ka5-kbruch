%define		kdeappsver	21.12.3
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kbruch
Summary:	Kbruch
Name:		ka5-%{kaname}
Version:	21.12.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	da21a38998014aff90c675e036b4605e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KBruch is a small program to practice calculating with fractions and
percentages. Different exercises are provided for this purpose and you
can use the learning mode to practice with fractions. The program
checks the user's input and gives feedback.

%description -l pl.UTF-8
KBruch to mały program do ćwiczenia obliczeń na ułamkach i procentach.
W tym celu program podaje różne ćwiczenia, dzięki którym możesz
trenować operacje na ułamkach w trybie nauki. KBruch sprawdza
odpowiedzi użytkownika i podaje informacje zwrotne.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kbruch
%{_desktopdir}/org.kde.kbruch.desktop
%{_datadir}/config.kcfg/kbruch.kcfg
%{_iconsdir}/hicolor/16x16/apps/kbruch.png
%{_iconsdir}/hicolor/22x22/apps/kbruch.png
%{_iconsdir}/hicolor/32x32/apps/kbruch.png
%{_iconsdir}/hicolor/48x48/apps/kbruch.png
%{_iconsdir}/hicolor/64x64/apps/kbruch.png
%{_iconsdir}/hicolor/scalable/apps/kbruch.svgz
%{_datadir}/kbruch
%{_datadir}/kxmlgui5/kbruch
%lang(ca) %{_mandir}/ca/man1/kbruch.1*
%lang(de) %{_mandir}/de/man1/kbruch.1*
%lang(es) %{_mandir}/es/man1/kbruch.1*
%lang(et) %{_mandir}/et/man1/kbruch.1*
%lang(it) %{_mandir}/it/man1/kbruch.1*
%{_mandir}/man1/kbruch.1*
%lang(nl) %{_mandir}/nl/man1/kbruch.1*
%lang(pt) %{_mandir}/pt/man1/kbruch.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kbruch.1*
%lang(ru) %{_mandir}/ru/man1/kbruch.1*
%lang(sv) %{_mandir}/sv/man1/kbruch.1*
%lang(uk) %{_mandir}/uk/man1/kbruch.1*
%{_datadir}/metainfo/org.kde.kbruch.appdata.xml
%lang(fr) %{_mandir}/fr/man1/kbruch.1*
