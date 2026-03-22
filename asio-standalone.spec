%global tag_version 1-30-2
Name:           asio-standalone
Version:        1.30.2
Release:        1%{?dist}
Summary:        Standalone Asio C++ library (no Boost)
License:        BSL-1.0
URL:            https://think-async.com/
Source0:        https://github.com/chriskohlhoff/asio/archive/refs/tags/asio-%{tag_version}.tar.gz
BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

Conflicts:      asio-devel

%description
Standalone Asio header-only library without Boost dependency.

%prep
%autosetup -n asio-asio-%{tag_version}

%build
cd asio
./autogen.sh
%configure --without-boost

%install
cd asio
mkdir -p %{buildroot}%{_includedir}
cp -pr include/* %{buildroot}%{_includedir}/
find %{buildroot}%{_includedir} -name "Makefile*" -delete

mkdir -p %{buildroot}%{_datadir}/pkgconfig
cp asio.pc %{buildroot}%{_datadir}/pkgconfig/asio.pc

%files
%{_includedir}/asio.hpp
%{_includedir}/asio/
%{_datadir}/pkgconfig/asio.pc
%license LICENSE_1_0.txt

%changelog
* Sun Mar 22 2026 Your Name <mayafluxcollective@proton.me> - 1.30.2-2
- Initial standalone build for MayaFlux (No-Boost)
