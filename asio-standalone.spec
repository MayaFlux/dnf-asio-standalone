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
BuildRequires:  pkgconfig

Conflicts:      asio-devel

%description
Standalone Asio header-only library without Boost dependency.

%prep
%setup -q -n asio-asio-%{tag_version}

%build
(
  cd asio
  ./autogen.sh
  %configure --without-boost
)

%install
(
  cd asio
  %make_install
)

rm -rf %{buildroot}%{_datadir}/doc/asio

%files
%license asio/LICENSE_1_0.txt
%{_includedir}/asio.hpp
%{_includedir}/asio/
%{_datadir}/pkgconfig/asio.pc

%changelog
* Sun Mar 22 2026 Your Name <mayafluxcollective@proton.me> - 1.30.2-2
- Initial standalone build for MayaFlux (No-Boost)
