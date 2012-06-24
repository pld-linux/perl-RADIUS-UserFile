%include	/usr/lib/rpm/macros.perl
%define	pdir	RADIUS
%define	pnam	UserFile
Summary:	RADIUS::UserFile perl module
Summary(pl):	Modu� perla RADIUS::UserFile
Name:		perl-RADIUS-UserFile
Version:	1.01
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3fd8852d4440aa950098a28f6b788fc
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Tie-IxHash
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RADIUS::UserFile - module for manipulating a RADIUS users file.

%description -l pl
RADIUS::UserFile - modu� do operowania na bazie danych u�ytkownik�w
RADIUS-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
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
%{perl_vendorlib}/RADIUS/UserFile.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
