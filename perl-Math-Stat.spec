%define module	Math-Stat

Name:		perl-%{module}
Version:	0.1
Release:	11
Summary:	Perform Sample Statistics on Arrays
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Math/%{module}-%{version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This package provides sample statistics on arrays.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes
%{perl_vendorlib}/Math
%{perl_vendorlib}/auto/Math
%{_mandir}/*/*

%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1-8mdv2010.0
+ Revision: 430501
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.1-7mdv2009.0
+ Revision: 257817
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.1-6mdv2009.0
+ Revision: 245871
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1-4mdv2008.1
+ Revision: 136285
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-4mdv2008.0
+ Revision: 86637
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-3mdv2007.0
- Rebuild

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.1-2mdk
- Fix According to perl Policy
	- Source URL

* Fri Oct 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.1-1mdk
- first mdk release

