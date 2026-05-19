%define module decorator

Name:		python-decorator
Summary:	Python decorator utilities
Version:	5.3.1
Release:	1
License:	BSD-2-Clause
Group:		Development/Python
URL:		https://pypi.python.org/pypi/decorator/
Source0:	https://github.com/micheles/decorator/archive/%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)

%description
The aim of the decorator module it to simplify the usage of decorators
for the average programmer, and to popularize decorators by showing
various non-trivial examples. Of course, as all techniques, decorators
can be abused and you should not try to solve every problem with a
decorator, just because you can.

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
