%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	GHTTP
Summary:	Perl interface to the gnome ghttp library
Summary(pl):	Modu³ perla z interfejsem do biblioteki gnome ghttp
Name:		perl-HTTP-GHTTP
Version:	1.07
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	libghttp-devel
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to the gnome ghttp library.

%description -l pl
Modu³ perla z interfejsem do biblioteki GNOME ghttp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
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
%dir %{perl_sitearch}/HTTP
%{perl_sitearch}/HTTP/GHTTP.pm
%dir %{perl_sitearch}/auto/HTTP
%{perl_sitearch}/auto/HTTP/GHTTP
%{_mandir}/man3/*
