#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : google-auth-oauthlib
Version  : 0.4.5
Release  : 11
URL      : https://files.pythonhosted.org/packages/16/92/fd6a1d55cb152e3e9d5fa06eeb1c65ad91195a1a2fceccdef7e6fbc36a00/google-auth-oauthlib-0.4.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/16/92/fd6a1d55cb152e3e9d5fa06eeb1c65ad91195a1a2fceccdef7e6fbc36a00/google-auth-oauthlib-0.4.5.tar.gz
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
oauthlib integration for Google Auth
====================================
|pypi|

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
%setup -q -n google-auth-oauthlib-0.4.5
cd %{_builddir}/google-auth-oauthlib-0.4.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1627684994
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/google-auth-oauthlib
cp %{_builddir}/google-auth-oauthlib-0.4.5/LICENSE %{buildroot}/usr/share/package-licenses/google-auth-oauthlib/2b8b815229aa8a61e483fb4ba0588b8b6c491890
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
/usr/share/package-licenses/google-auth-oauthlib/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
