Summary:	-
Summary(pl):	-
Name:		stardust
Version:	0.1.10
Release:	0.1
License:	GPL	
Group:		X11/Applications/Games
Source0:	http://download.gna.org/stardust/%{name}-%{version}.tar.gz
# Source0-md5:	2b064ec153bb384e914ffe7362648f3e
URL:		https://gna.org/projects/stardust/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of Stardust is to create a 3D space flight simulator. It is portable and expandable, and it simulates the kinematics of space flight.

%description -l pl

%prep
%setup -q

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
glib-gettextize
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_prefix}/games/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/games/%{name}
