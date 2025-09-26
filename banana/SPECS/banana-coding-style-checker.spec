Name:           epiclang-plugin-banana
Version:        1.0.0
Release:        1%{?dist}
Summary:        Epitech C coding style checker

License:       	GPL 
Source0:	%{name}-%{version}.tar.gz

%description
Epitech C coding style checker

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
