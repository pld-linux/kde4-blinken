%define         _state          stable
%define         orgname         blinken
#
Summary:	KDE version of the well-known game Simon Says
Summary(pl.UTF-8):	Wersja KDE dobrze znanej gry "Simon Says"
Name:		kde4-blinken
Version:	4.12.0
Release:	1
License:	LGPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	cb90541e2d0bfad581be9ab40d32508a
URL:		http://www.kde.org/
BuildRequires:	kde4-kdelibs-devel >= %{version}
Obsoletes:	kde4-kdeedu-blinken < 4.6.99
Obsoletes:	blinken < 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE version of the well-known game Simon Says.

%description -l pl.UTF-8
Wersja KDE dobrze znanej gry "Simon Says".

%prep
%setup -q -n %{orgname}-%{version}

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

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/blinken
%{_desktopdir}/kde4/blinken.desktop
%{_datadir}/apps/blinken
%{_datadir}/config.kcfg/blinken.kcfg
%{_iconsdir}/*/*/apps/blinken.*
