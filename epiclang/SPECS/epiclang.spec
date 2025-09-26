Name:           epiclang
Version:        1.0.0
Release:        1%{?dist}
Summary:        compiler for Epitech C projects
Source0: 	epiclang
Source1:	epiclang.py

License:       	GPL 

Requires: clang >= 20
Requires: python3 >= 3.11

%description
epiclang is the compiler wrapper used to compile Epitech C projects.

It is a wrapper around clang-20 that loads the plug-ins installed in /usr/lib/epiclang/plugins and /usr/local/lib/epiclang/plugins

%prep

%install
mkdir -p %{buildroot}/usr/local/bin
cp %{SOURCE0} %{buildroot}/usr/local/bin/
cp %{SOURCE1} %{buildroot}/usr/local/bin/

%files
/usr/local/bin/%{name}
/usr/local/bin/%{name}.py

%changelog
* Tue Sep 24 2025 epiclang rpm package base on offical ppa
- 
