%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	GHTTP
Summary:	Perl interface to the gnome ghttp library
Summary(pl):	Modu³ perla z interfejsem do biblioteki gnome ghttp
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
Perl interface to the gnome ghttp library.

%description -l pl
Modu³ perla z interfejsem do biblioteki GNOME ghttp.

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
