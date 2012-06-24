%include	/usr/lib/rpm/macros.perl
Summary:	RADIUS-UserFile perl module
Summary(pl):	Modu� perla RADIUS-UserFile
Name:		perl-RADIUS-UserFile
Version:	0.98
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/RADIUS/RADIUS-UserFile-%{version}.tar.gz
Patch0:		perl-RADIUS-UserFile-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RADIUS-UserFile - module for manipulating a RADIUS users file.

%description -l pl
RADIUS-UserFile - modu� do operowania na bazie danych u�ytkownik�w
RADIUSa.

%prep
%setup -q -n RADIUS-UserFile-%{version}
%patch -p0

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}-%{version}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/RADIUS/UserFile
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README BUGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README,BUGS}.gz

%{perl_sitelib}/RADIUS/UserFile.pm
%{perl_sitearch}/auto/RADIUS/UserFile

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}-%{version}
