%include	/usr/lib/rpm/macros.perl
Summary:	Perl interface to the gnome ghttp library 
Summary(pl):	Modu� perla z interfejsem na bibliotek� gnome ghttp
Name:		perl-HTTP-GHTTP
Version:	1.06
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTP/HTTP-GHTTP-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	libghttp-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl interface to the gnome ghttp library.

%description -l pl
Modu� perla z interfejsem na bibliotek� gnome ghttp.

%prep
%setup -q -n HTTP-GHTTP-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

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
%{perl_sitearch}/HTTP/GHTTP.pm
%attr(755,root,root) %{perl_sitearch}/auto/HTTP/GHTTP/*.so
%{_mandir}/man3/*
