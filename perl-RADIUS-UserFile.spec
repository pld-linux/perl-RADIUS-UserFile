%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	RADIUS-UserFile perl module
Summary(pl):	Modu³ perla RADIUS-UserFile
Name:		perl-RADIUS-UserFile
Version:	0.98
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/RADIUS/RADIUS-UserFile-%{version}.tar.gz
Patch:		perl-RADIUS-UserFile-paths.patch
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
RADIUS-UserFile - module for manipulating a RADIUS users file. 

%description -l pl
RADIUS-UserFile - modu³ do operowania na bazie danych u¿ytkowników RADIUSa.

%prep
%setup -q -n RADIUS-UserFile-%{version}
%patch -p0

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/src/%{name}-%{version}

make install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT/usr/src/%{name}-%{version}

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

/usr/src/%{name}-%{version}
