#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	RADIUS
%define		pnam	UserFile
%include	/usr/lib/rpm/macros.perl
Summary:	RADIUS::UserFile perl module
Summary(pl.UTF-8):	Moduł perla RADIUS::UserFile
Name:		perl-RADIUS-UserFile
Version:	1.01
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3fd8852d4440aa950098a28f6b788fc
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/RADIUS-UserFile/
BuildRequires:	perl-Tie-IxHash
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RADIUS::UserFile - module for manipulating a RADIUS users file.

%description -l pl.UTF-8
RADIUS::UserFile - moduł do operowania na bazie danych użytkowników
RADIUS-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README BUGS
%{perl_vendorlib}/RADIUS/UserFile.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
