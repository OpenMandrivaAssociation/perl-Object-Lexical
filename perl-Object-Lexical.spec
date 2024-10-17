%define upstream_name    Object-Lexical
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Object::Lexical - Syntactic Sugar for Easy Object Instance Data &
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{upstream_name}
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(PadWalker)
BuildArch:	noarch

%description
Object::Lexical provides syntactic sugar to create objects.
Normal "my" variables are used for instance data. $this is
automatically read off of the argument stack. This follows "real"
OO languages, where user code need not concern itself with
helping the language implement objects.  Normal OO Perl code is
ugly, hard to read, tedious to type, and error prone.  The
"$self-"{field}> syntax is cumbersome, and using an object field
with a built in, like "push()", requires syntax beyond novice
Perl programmers: "push @{$self-"{field}}, $value>.  Spelling
field names wrong results in hard to find bugs: the hash
autovivicates, and no "variables must be declared" warning is
issued.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Object/Lexical.pm
%{_mandir}/*/*


%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 401999
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-4mdv2009.0
+ Revision: 241805
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-2mdv2008.0
+ Revision: 86721
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.02-1mdk
- initial Mandriva package

