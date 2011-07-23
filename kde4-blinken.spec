Summary:	KDE version of the well-known game Simon Says
Summary(pl.UTF-8):	Wersja KDE dobrze znanej gry "Simon Says"
Name:		blinken
Version:	4.7.0
Release:	0.1
License:	LGPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	54b20e46c875c544bde5a6adff53af99
URL:		http://www.kde.org/
Obsoletes:	kde4-kdeedu-blinken
# BR: something that provides kfontutils.h
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
