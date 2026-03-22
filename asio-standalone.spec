Name:           asio-standalone
Version:        1.30.2
Release:        1%{?dist}
Summary:        Standalone Asio C++ library (no Boost)
License:        BSL-1.0
URL:            https://think-async.com/
Source0:        https://github.com/chriskohlhoff/asio/archive/refs/tags/asio-%{version}.tar.gz
BuildArch:      noarch

# This prevents dnf from trying to install this alongside the official asio-devel
Conflicts:      asio-devel

%description
Standalone Asio header-only library without Boost dependency.

%prep
%autosetup -n asio-asio-%{version}

%build
# Header-only: nothing to do.

%install
mkdir -p %{buildroot}%{_includedir}
# Copy everything from the include directory
cp -pr asio/include/* %{buildroot}%{_includedir}/

%files
%{_includedir}/asio.hpp
%{_includedir}/asio/
%license asio/LICENSE_1_0.txt
