%include	/usr/lib/rpm/macros.perl
Summary:	Perl interface to the gnome ghttp library 
Summary(pl):	Modu³ perla z interfejsem na bibliotekê gnome ghttp
Name:		perl-HTTP-GHTTP
Version:	1.06
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTP/HTTP-GHTTP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	libghttp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to the gnome ghttp library.

%description -l pl
Modu³ perla z interfejsem na bibliotekê gnome ghttp.

%prep
%setup -q -n HTTP-GHTTP-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/g-request
%dir %{perl_sitearch}/HTTP
%{perl_sitearch}/HTTP/GHTTP.pm
%dir %{perl_sitearch}/auto/HTTP
%dir %{perl_sitearch}/auto/HTTP/GHTTP
%attr(755,root,root) %{perl_sitearch}/auto/HTTP/GHTTP/*.so
%{_mandir}/man3/*
