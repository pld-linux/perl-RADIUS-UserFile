%define	pdir	RADIUS
%define	pnam	UserFile
%include	/usr/lib/rpm/macros.perl
Summary:	RADIUS-UserFile perl module
Summary(pl):	Modu³ perla RADIUS-UserFile
Name:		perl-RADIUS-UserFile
Version:	0.99
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RADIUS-UserFile - module for manipulating a RADIUS users file.

%description -l pl
RADIUS-UserFile - modu³ do operowania na bazie danych u¿ytkowników
RADIUSa.

%prep
%setup -q -n RADIUS-UserFile-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf Changes README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/RADIUS/UserFile.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
