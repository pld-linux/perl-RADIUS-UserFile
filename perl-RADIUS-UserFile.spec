%include	/usr/lib/rpm/macros.perl
%define	pdir	RADIUS
%define	pnam	UserFile
Summary:	RADIUS::UserFile perl module
Summary(pl):	Modu³ perla RADIUS::UserFile
Name:		perl-RADIUS-UserFile
Version:	1.01
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Tie-IxHash
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RADIUS::UserFile - module for manipulating a RADIUS users file.

%description -l pl
RADIUS::UserFile - modu³ do operowania na bazie danych u¿ytkowników
RADIUS-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README BUGS
%{perl_sitelib}/RADIUS/UserFile.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
