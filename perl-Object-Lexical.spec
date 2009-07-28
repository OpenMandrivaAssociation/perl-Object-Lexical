%define upstream_name    Object-Lexical
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	Object::Lexical - Syntactic Sugar for Easy Object Instance Data &
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-PadWalker
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Object/Lexical.pm
%{_mandir}/*/*
