%define		_realname	xmms-status-plugin

Summary:	A docklet for XMMS
Summary(pl.UTF-8):	Docklet dla XMMS
Name:		xmms-general-status
Version:	1.0
Release:	4
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www.hellion.org.uk/source/%{_realname}-%{version}.tar.gz
# Source0-md5:	055a0317b2d224583e463ab0942c91d5
URL:		http://www.hellion.org.uk/xmms-status-plugin/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Provides:	xmms-status-plugin = %{version}-%{release}
Obsoletes:	xmms-status-plugin <= 1.0-2
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A status docklet for XMMS, docks into the GNOME Status dock.

%description -l pl.UTF-8
Pakiet zawiera docklet dla XMMS-a, który pokazuje status na pasku
GNOME.

%prep
%setup -q -n %{_realname}-%{version}

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{_realname}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_realname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{xmms_general_plugindir}/libstatusdocklet.so
%{xmms_general_plugindir}/libstatusdocklet.la
%{xmms_datadir}/status_docklet
