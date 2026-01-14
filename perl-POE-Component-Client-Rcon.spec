#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	POE
%define		pnam	Component-Client-Rcon
Summary:	POE::Component::Client::Rcon - implementation of the Rcon remote console protocol
Summary(pl.UTF-8):	POE::Component::Client::Rcon - implementacja protokołu zdalnej konsoli Rcon
Name:		perl-POE-Component-Client-Rcon
Version:	0.23
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ebff9d4943f80cbd147e37d4dbf7a35a
URL:		http://search.cpan.org/dist/POE-Component-Client-Rcon/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.15
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Client::Rcon is an implementation of the Rcon protocol
- the protocol commonly used to remotely administer Half-Life, Quake,
and RTCW (Return to Castle Wolfenstein) servers. It is capable of
handling multiple Rcon requests simultaneously, even multiple requests
to the same IP/Port simultaneously.

%description -l pl.UTF-8
POE::Component::Client::RCon to implementacja protokołu Rcon -
powszechnie używanego do zdalnego administrowania serwerami Half-Life,
Quake'a czy RTCW (Return to Castle Wolfenstein). Umożliwia jednoczesną
obsługę wielu żądań RCon, a nawet jednoczesne żądania do tego samego
IP/portu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/POE/Component/Client/*.pm
%{_mandir}/man3/*
