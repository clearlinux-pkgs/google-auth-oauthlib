#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-auth-oauthlib
Version  : 0.4.1
Release  : 8
URL      : https://files.pythonhosted.org/packages/cd/5a/2b5a4c1294a4e8903bdba122083bd505dc51688a95d4670cde89dc45e6ed/google-auth-oauthlib-0.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/cd/5a/2b5a4c1294a4e8903bdba122083bd505dc51688a95d4670cde89dc45e6ed/google-auth-oauthlib-0.4.1.tar.gz
Summary  : Google Authentication Library
Group    : Development/Tools
License  : Apache-2.0
Requires: google-auth-oauthlib-bin = %{version}-%{release}
Requires: google-auth-oauthlib-license = %{version}-%{release}
Requires: google-auth-oauthlib-python = %{version}-%{release}
Requires: google-auth-oauthlib-python3 = %{version}-%{release}
Requires: click
Requires: google-auth
Requires: requests-oauthlib
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : google-auth
BuildRequires : requests-oauthlib

%description
====================================
        
        |pypi|
        
        This library provides `oauthlib`_ integration with `google-auth`_.

%package bin
Summary: bin components for the google-auth-oauthlib package.
Group: Binaries
Requires: google-auth-oauthlib-license = %{version}-%{release}

%description bin
bin components for the google-auth-oauthlib package.


%package license
Summary: license components for the google-auth-oauthlib package.
Group: Default

%description license
license components for the google-auth-oauthlib package.


%package python
Summary: python components for the google-auth-oauthlib package.
Group: Default
Requires: google-auth-oauthlib-python3 = %{version}-%{release}

%description python
python components for the google-auth-oauthlib package.


%package python3
Summary: python3 components for the google-auth-oauthlib package.
Group: Default
Requires: python3-core
Provides: pypi(google_auth_oauthlib)
Requires: pypi(google_auth)
Requires: pypi(requests_oauthlib)

%description python3
python3 components for the google-auth-oauthlib package.


%prep
%setup -q -n google-auth-oauthlib-0.4.1
cd %{_builddir}/google-auth-oauthlib-0.4.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602821585
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/google-auth-oauthlib
cp %{_builddir}/google-auth-oauthlib-0.4.1/LICENSE %{buildroot}/usr/share/package-licenses/google-auth-oauthlib/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/google-oauthlib-tool

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/google-auth-oauthlib/7df059597099bb7dcf25d2a9aedfaf4465f72d8d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
