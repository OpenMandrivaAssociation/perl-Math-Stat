%define module	Math-Stat
%define name	perl-%{module}
%define version 0.1
%define release %mkrel 6

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:	    Perform Sample Statistics on Arrays
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Math/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
Buildrequires:  perl-devel
%endif
Buildarch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This package provides sample statistics on arrays.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Math
%{perl_vendorlib}/auto/Math
%{_mandir}/*/*

