Summary:	KoolDock is a dock for KDE with cool visual enhancements and effects
Name:		kooldock
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		KDE/Applications
Source0:	http://ktown.kde.cl/kooldock/dist/%{name}-%{version}.tar.gz
# Source0-md5:	a53b74ce56f65b738413205cd9bfe2ca
URL:		http://ktown.kde.cl/kooldock/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040805
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KoolDock is a dock for KDE with cool visual enhancements and effects. 
KoolDock is a fork of the original work of Dang Viet Dung, KSmoothDock
Some of it features are:
 - Display quick launchers to your favourite apps
 - A builtin task bar
 - Pager and clock. (Not done yet)
 - Smooth zooming effect (like Apple's OS X dock)
 - Transparent Background

%prep
%setup -q -n %{name}

%build
cp -f /usr/share/automake/config.sub admin

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/*/*/apps/%{name}.png
%{_datadir}/apps/%{name}
