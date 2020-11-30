%define module	decorator

Summary:	Python decorator utilities
Name:		python-%{module}
Version:	4.4.2
Release:	1
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/decorator/
Source0:	https://github.com/micheles/decorator/archive/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python2-pkg-resources
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	python2-setuptools

%description
The aim of the decorator module it to simplify the usage of decorators
for the average programmer, and to popularize decorators by showing
various non-trivial examples. Of course, as all techniques, decorators
can be abused and you should not try to solve every problem with a
decorator, just because you can.

%package -n python2-decorator
Summary:	Python2 decorator utilities
Group:		Development/Python
Requires:	python2
 
%description -n python2-decorator
The aim of the decorator module it to simplify the usage of decorators
for the average programmer, and to popularize decorators by showing
various non-trivial examples. Of course, as all techniques, decorators
can be abused and you should not try to solve every problem with a
decorator, just because you can.

%prep
%setup -q -c
mv %{module}-%{version} python2
cp -r python2 python

%install
cd python2
%{__python2} setup.py install --root=%{buildroot}
cd -

cd python
%{__python} setup.py install --root=%{buildroot}
cd -

%files -n python2-decorator 
%doc python2/*.txt
%{python2_sitelib}/%{module}-%{version}-*.egg-info
%{python2_sitelib}/%{module}.py*

%files
%{python_sitelib}/%{module}-%{version}-*.egg-info
%{python_sitelib}/%{module}.py*
%{python_sitelib}/__pycache__/
