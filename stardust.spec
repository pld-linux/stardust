# ToDo:
# - verify BuildRequires (I used quick'n'dirty script for that)
Summary:	3D space flight simulator
Summary(pl):	Trójwymiarowy symulator lotów kosmicznych
Name:		stardust
Version:	0.1.12
Release:	1
License:	GPL	
Group:		X11/Applications/Games
Source0:	http://download.gna.org/stardust/%{name}-%{version}.tar.gz
# Source0-md5:	995474d9fb2461cb8882689719e1f62a
URL:		https://gna.org/projects/stardust/
BuildRequires:	SDL-devel
BuildRequires:	STLport-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	wxWindows-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of Stardust is to create a 3D space flight simulator. It is
portable and expandable, and it simulates the kinematics of space
flight.

%description -l pl
Celem projektu Stardust jest stworzenie trójwymiarowego symulatora lotów
kosmicznych. Jest on przeno¶ny i ³atwo rozszerzalny, oraz symuluje
kinematykê lotów kosmicznych.

%prep
%setup -q

%build
glib-gettextize --copy --force
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
