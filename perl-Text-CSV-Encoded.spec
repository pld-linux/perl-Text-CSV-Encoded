#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Text
%define	pnam	CSV-Encoded
Summary:	Text::CSV::Encoded - encoding aware Text::CSV
Summary(pl.UTF-8):	Text::CSV::Encoded - wersja Text::CSV obsługująca kodowania
Name:		perl-Text-CSV-Encoded
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ed745eb7a416818b9c129eced8af93d
URL:		http://search.cpan.org/dist/Text-CSV-Encoded/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Text-CSV >= 1.12
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module inherits Text::CSV and is aware of input/output encodings.

%description -l pl.UTF-8
Ten moduł dziedziczy po Text::CSV i obsługuje kodowania
wejścia/wyjścia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Text/CSV/Encoded.pm
%{perl_vendorlib}/Text/CSV/Encoded
%{_mandir}/man3/Text::CSV::Encoded*.3pm*
