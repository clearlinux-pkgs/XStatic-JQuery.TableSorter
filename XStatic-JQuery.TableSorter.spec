#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-JQuery.TableSorter
Version  : 2.14.5.1
Release  : 19
URL      : http://pypi.debian.net/XStatic-JQuery.TableSorter/XStatic-JQuery.TableSorter-2.14.5.1.tar.gz
Source0  : http://pypi.debian.net/XStatic-JQuery.TableSorter/XStatic-JQuery.TableSorter-2.14.5.1.tar.gz
Summary  : JQuery.TableSorter 2.14.5 (XStatic packaging standard)
Group    : Development/Tools
License  : GPL-2.0+ MIT
Requires: XStatic-JQuery.TableSorter-python3
Requires: XStatic-JQuery.TableSorter-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
--------------
        
        JQuery.TableSorter JavaScript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-JQuery.TableSorter package.
Group: Default
Requires: XStatic-JQuery.TableSorter-python3
Provides: xstatic-jquery.tablesorter-python

%description python
python components for the XStatic-JQuery.TableSorter package.


%package python3
Summary: python3 components for the XStatic-JQuery.TableSorter package.
Group: Default
Requires: python3-core

%description python3
python3 components for the XStatic-JQuery.TableSorter package.


%prep
%setup -q -n XStatic-JQuery.TableSorter-2.14.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532214632
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
