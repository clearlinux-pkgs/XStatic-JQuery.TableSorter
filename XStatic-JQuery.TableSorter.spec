#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-JQuery.TableSorter
Version  : 2.14.5.1
Release  : 23
URL      : http://pypi.debian.net/XStatic-JQuery.TableSorter/XStatic-JQuery.TableSorter-2.14.5.1.tar.gz
Source0  : http://pypi.debian.net/XStatic-JQuery.TableSorter/XStatic-JQuery.TableSorter-2.14.5.1.tar.gz
Summary  : JQuery.TableSorter 2.14.5 (XStatic packaging standard)
Group    : Development/Tools
License  : GPL-2.0+ MIT
Requires: XStatic-JQuery.TableSorter-python = %{version}-%{release}
Requires: XStatic-JQuery.TableSorter-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
XStatic-JQuery.TableSorter
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
Requires: XStatic-JQuery.TableSorter-python3 = %{version}-%{release}
Provides: xstatic-jquery.tablesorter-python

%description python
python components for the XStatic-JQuery.TableSorter package.


%package python3
Summary: python3 components for the XStatic-JQuery.TableSorter package.
Group: Default
Requires: python3-core
Provides: pypi(XStatic-JQuery.TableSorter)

%description python3
python3 components for the XStatic-JQuery.TableSorter package.


%prep
%setup -q -n XStatic-JQuery.TableSorter-2.14.5.1
cd %{_builddir}/XStatic-JQuery.TableSorter-2.14.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582851028
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
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
