#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Client-Rcon
Summary:	POE::Component::Client::Rcon - implementation of the Rcon remote console protocol
Summary(pl):	POE::Component::Client::Rcon - implementacja protoko³u zdalnej konsoli Rcon
Name:		perl-POE-Component-Client-Rcon
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9cda8dd376ee5f85e122f75a78bfbd83
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-POE >= 0.15
BuildRequires:	perl-Time-HiRes
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Client::Rcon is an implementation of the Rcon protocol
- the protocol commonly used to remotely administer Half-Life, Quake,
and RTCW (Return to Castle Wolfenstein) servers. It is capable of
handling multiple Rcon requests simultaneously, even multiple requests
to the same IP/Port simultaneously.

%description -l pl
POE::Component::Client::RCon to implementacja protoko³u Rcon -
powszechnie u¿ywanego do zdalnego administrowania serwerami Half-Life,
Quake'a czy RTCW (Return to Castle Wolfenstein). Umo¿liwia jednoczesn±
obs³ugê wielu ¿±dañ RCon, a nawet jednoczesne ¿±dania do tego samego
IP/portu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
