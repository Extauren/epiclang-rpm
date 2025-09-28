Name:           epiclang-plugin-banana
Version:        1.0.0
Release:        1%{?dist}
Summary:        Epitech C coding style checker

License:       	GPL 
Source0:	https://github.com/Extauren/epiclang-rpm/raw/refs/heads/main/epiclang-plugin-banana-1.0.0.tar.gz

%description
Epitech C coding style checker

%define debug_package %{nil}

%prep
%setup -q

%install
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/local/lib/epiclang/plugins
cp %{name}.so %{buildroot}/usr/local/lib/epiclang/plugins

%files
/usr/local/lib/epiclang/plugins/%{name}.so

%changelog
* Tue Sep 23 2025 create first epiclang-plugin-banana.so rpm package
- 
