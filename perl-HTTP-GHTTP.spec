%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	GHTTP
Summary:	HTTP::GHTTP - Perl interface to the GNOME ghttp library
Summary(pl):	HTTP::GHTTP - modu� Perla z interfejsem do biblioteki GNOME ghttp
Name:		perl-HTTP-GHTTP
Version:	1.07
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af6090669fde7709c765c2caf03aa42b
BuildRequires:	libghttp-devel
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTTP::GHTTP module is a simple Perl interface to the GNOME ghttp
library. It allows you to make very simple HTTP requests, without the
weight of something like LWP. This makes it very useful in situations
where memory and speed are at a premium, such as mod_perl.

%description -l pl
Modu� Perla HTTP::GHTTP stanowi prosty interfejs do biblioteki GNOME
ghttp. Umo�liwia on tworzenie bardzo prostych zapyta� HTTP bez narzutu
czego� takiego, jak LWP. Czyni to go bardzo przydatnym, gdy pami�� i
pr�dko�� s� bardzo istotne, np. w mod_perl.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/g-request
%dir %{perl_vendorarch}/HTTP
%{perl_vendorarch}/HTTP/GHTTP.pm
%dir %{perl_vendorarch}/auto/HTTP
%{perl_vendorarch}/auto/HTTP/GHTTP
%{_mandir}/man3/*
