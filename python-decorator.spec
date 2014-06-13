%define module	decorator

Summary:	Python decorator utilities
Name:		python-%{module}
Version:	3.4.0
Release:	7
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/decorator/
Source0:	http://pypi.python.org/packages/source/d/decorator/decorator-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)

%description
The aim of the decorator module it to simplify the usage of decorators
for the average programmer, and to popularize decorators by showing
various non-trivial examples. Of course, as all techniques, decorators
can be abused and you should not try to solve every problem with a
decorator, just because you can.

%package -n python3-decorator
Summary:	Python decorator utilities
Group:		Development/Python
Requires:	python3
 
%description -n python3-decorator
The aim of the decorator module it to simplify the usage of decorators
for the average programmer, and to popularize decorators by showing
various non-trivial examples. Of course, as all techniques, decorators
can be abused and you should not try to solve every problem with a
decorator, just because you can.

%prep
%setup -q -c
mv %{module}-%{version} python2
cp -r python2 python3

%install
pushd python2
%{__python} setup.py install --root=%{buildroot}
popd

pushd python3
%{__python3} setup.py install --root=%{buildroot}
popd

%files -n python-decorator 
%doc python2/documentation.* python2/*.txt
%{python_sitelib}/%{module}*

%files -n python3-decorator
%doc python3/documentation.* python3/*.txt
%{python3_sitelib}/%{module}*

