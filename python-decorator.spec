%define module	decorator
%define name	python-%{module}
%define version	3.3.3
%define release %mkrel 1

Summary:	Python decorator utilities
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/d/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/decorator/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel

%description
The aim of the decorator module it to simplify the usage of decorators
for the average programmer, and to popularize decorators by showing
various non-trivial examples. Of course, as all techniques, decorators
can be abused and you should not try to solve every problem with a
decorator, just because you can.

%prep 
%setup -q -n %{module}-%{version}

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} 

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt documentation.*
%py_sitedir/%{module}*
