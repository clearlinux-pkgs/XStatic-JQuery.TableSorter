#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-JQuery.TableSorter
Version  : 2.14.5.1
Release  : 11
URL      : https://pypi.python.org/packages/source/X/XStatic-JQuery.TableSorter/XStatic-JQuery.TableSorter-2.14.5.1.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-JQuery.TableSorter/XStatic-JQuery.TableSorter-2.14.5.1.tar.gz
Summary  : JQuery.TableSorter 2.14.5 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT GPL-2.0+
Requires: XStatic-JQuery.TableSorter-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-JQuery.TableSorter
--------------
JQuery.TableSorter JavaScript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-JQuery.TableSorter package.
Group: Default

%description python
python components for the XStatic-JQuery.TableSorter package.


%prep
%setup -q -n XStatic-JQuery.TableSorter-2.14.5.1

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
