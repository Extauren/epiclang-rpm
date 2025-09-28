Name:           epiclang
Version:        1.0.0
Release:        1%{?dist}
Summary:        compiler for Epitech C projects
Source0: 	https://github.com/Extauren/epiclang-rpm/raw/refs/heads/main/epiclang-1.0.0.tar.gz

License:       	GPL

Requires: clang >= 20
Requires: python3 >= 3.11
Requires: epiclang-plugin-banana

%description
epiclang is the compiler wrapper used to compile Epitech C projects.

It is a wrapper around clang-20 that loads the plug-ins installed in /usr/lib/epiclang/plugins and /usr/local/lib/epiclang/plugins

%define debug_package %{nil}

%prep
%setup -q

%install
mkdir -p %{buildroot}/usr/local/bin
cp %{name} %{buildroot}/usr/local/bin/
cp %{name}.py %{buildroot}/usr/local/bin/

%files
/usr/local/bin/%{name}
/usr/local/bin/%{name}.py

%changelog
* Tue Sep 24 2025 epiclang rpm package base on offical ppa
- 
