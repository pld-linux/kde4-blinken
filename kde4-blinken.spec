%define         _state          stable
%define         orgname         okular
#
Summary:	KDE version of the well-known game Simon Says
Summary(pl.UTF-8):	Wersja KDE dobrze znanej gry "Simon Says"
Name:		blinken
Version:	4.7.1
Release:	1
License:	LGPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	188ff5ff5ca53a4383c919eec9299fbe
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdeedu-blinken < 4.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE version of the well-known game Simon Says.

%description -l pl.UTF-8
Wersja KDE dobrze znanej gry "Simon Says".

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DCONFIG_INSTALL_DIR=%{_datadir}/config \
	-DDATA_INSTALL_DIR=%{_datadir}/apps \
	-DKCFG_INSTALL_DIR=%{_datadir}/config.kcfg \
	-DMIME_INSTALL_DIR=/nogo \
	-DTEMPLATES_INSTALL_DIR=%{_datadir}/templates \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_DISTRIBUTION_TEXT="PLD-Linux" \
	-DKDE4_ENABLE_FINAL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blinken
%{_desktopdir}/kde4/blinken.desktop
%{_datadir}/apps/blinken
%{_datadir}/config.kcfg/blinken.kcfg
%{_iconsdir}/*/*/apps/blinken.*
