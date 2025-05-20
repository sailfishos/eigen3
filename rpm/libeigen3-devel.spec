%undefine __cmake_in_source_build

#define _with_check -DEIGEN_BUILD_TESTS=ON -DEIGEN_TEST_NO_FORTRAN=ON -DEIGEN_TEST_NOQT=ON

Name:           libeigen3-devel
License:        MPLv2.0 and LGPLv2+ and BSD
Summary:        Lightweight linear algebra C++ template library
Url:            https://github.com/sailfishos/eigen3
Version:        3.4.0
Release:        1
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  fdupes, cmake
BuildArch: noarch

%description
Eigen is a lightweight C++ template library for vector and matrix math,
a.k.a. linear algebra.

%prep
%autosetup -n %{name}-%{version}/eigen

%build
%cmake %{?_with_check} -DINCLUDE_INSTALL_DIR=%{_includedir}/eigen3
%cmake_build

%install
%cmake_install

%fdupes %{buildroot}/%{_includedir}

%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig
%if 0%{?_with_check:1}
( cd test; ctest )
%endif

%files
%doc COPYING.README COPYING.BSD COPYING.MPL2 COPYING.LGPL
%{_includedir}/eigen3/*
%{_datadir}/pkgconfig/*
%{_datadir}/eigen3/cmake/*
