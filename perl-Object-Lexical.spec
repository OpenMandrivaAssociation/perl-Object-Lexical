%define real_name Object-Lexical

Summary:	Object::Lexical - Syntactic Sugar for Easy Object Instance Data &
Name:		perl-%{real_name}
Version:	0.02
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-PadWalker
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
%setup -q -n %{real_name}-%{version} 

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


