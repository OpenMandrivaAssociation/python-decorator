%define module	decorator

Summary:	Python decorator utilities
Name:		python-%{module}
Version:	3.4.0
Release:	1
Source0:	http://pypi.python.org/packages/source/d/decorator/decorator-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://pypi.python.org/pypi/decorator/
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} 

%files
%doc *.txt documentation.*
%py_sitedir/%{module}*


%changelog
* Tue May 08 2012 Lev Givon <lev@mandriva.org> 3.3.3-1mdv2011.0
+ Revision: 797609
- Update to 3.3.3.

* Thu Sep 01 2011 Lev Givon <lev@mandriva.org> 3.3.2-1
+ Revision: 697703
- Update to 3.3.2.

* Thu Apr 28 2011 Lev Givon <lev@mandriva.org> 3.3.1-1
+ Revision: 660079
- Update to 3.3.1.

* Mon Jan 03 2011 Lev Givon <lev@mandriva.org> 3.3.0-1mdv2011.0
+ Revision: 628030
- Update to 3.3.0.

* Sun Nov 28 2010 Lev Givon <lev@mandriva.org> 3.2.1-1mdv2011.0
+ Revision: 602463
- Update to 3.2.1.

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 3.2.0-3mdv2011.0
+ Revision: 592309
- rebuild for python 2.7
- replace the obsolete %%py_requires macro and add BR python-devel

* Tue Jul 13 2010 Lev Givon <lev@mandriva.org> 3.2.0-2mdv2011.0
+ Revision: 551374
- Fix file list.
- Update to 3.2.0.

* Tue Sep 08 2009 Lev Givon <lev@mandriva.org> 3.1.2-1mdv2010.0
+ Revision: 434273
- import python-decorator



