Summary:	KoolDock - a dock for KDE with cool visual enhancements and effects
Summary(pl):	KoolDock - dok dla KDE z rozszerzeniami i efektami wizualnymi
Name:		kooldock
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		KDE/Applications
Source0:	http://kde-apps.org/content/files/50910-%{name}.tar.gz
# Source0-md5:	f7cad0e1b518c5c8be1b3f5c536807be
URL:		http://ktown.kde.cl/kooldock/
Patch0:		kde-ac260-lt.patch
Patch1:		%{name}-am110.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
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

%description -l pl
KoolDock to dok dla kDE z rozszerzeniami i efektami wizualnymi. Jest
to fork oryginalnego projektu KSmoothDock autorstwa Dang Viet Dunga.
Niektóre z mo¿liwo¶ci to:
- wy¶wietlanie przycisków szybkiego uruchomienia ulubionych aplikacji
- wbudowany pasek zadañ
- pager i zegar (jeszcze nie gotowe)
- efekt p³ynnego powiêkszania (jak w doku OS X Apple'a)
- przezroczyste t³o

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p0

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
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
