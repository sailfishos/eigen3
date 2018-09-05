#define _with_check -DEIGEN_BUILD_TESTS=ON -DEIGEN_TEST_NO_FORTRAN=ON -DEIGEN_TEST_NOQT=ON

Name:           libeigen3-devel
License:        MPLv2
Group:          Development/Libraries
Summary:        Lightweight linear algebra C++ template library
Url:            http://eigen.tuxfamily.org/
Version:        3.3.5
Release:        1
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  fdupes, cmake
#BuildRequires:  doxygen, graphviz
#BuildRequires:  tex(latex)
BuildArch: noarch

%description
Eigen is a lightweight C++ template library for vector and matrix math,
a.k.a. linear algebra.

%files
%defattr(-,root,root)
%{_includedir}/eigen3/*
%{_datadir}/pkgconfig/*
%{_datadir}/eigen3/cmake/*

%prep
%setup -q -n %{name}-%{version}/eigen

%build
if [ ! -d build ] ; then mkdir build ; fi
cd build
cmake -DCMAKE_INSTALL_PREFIX=/usr %{?_with_check} ..
make %{?_smp_mflags}
#make doc

%install
cd build
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_docdir}/eigen3
#cp -R doc/html %{buildroot}/%{_docdir}/eigen3
%fdupes %{buildroot}/%{_includedir}
#%fdupes %{buildroot}/%{_docdir}


%check
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig
#test "$(pkg-config --modversion eigen3)" = "%{version}"
%if 0%{?_with_check:1}
( cd test; ctest )
%endif
