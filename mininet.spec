%global _hardened_build 1

# This file is encoded in UTF-8.  -*- coding: utf-8 -*-
Summary:       Virtual network emulator
Name:          mininet
Epoch:         1
Version:       2.3.0d6
Release:       1%{?dist}
License:       Mininet %{version} License
URL:           http://mininet.org/
Source0:       https://github.com/mininet/mininet/archive/%{version}.tar.gz
Source1:       check-and-update.sh

BuildRequires: gcc
BuildRequires: help2man
BuildRequires: make
BuildRequires: python-unversioned-command
BuildRequires: python3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

Requires:      ethtool
Requires:      iperf
Requires:      iproute
Requires:      libcgroup-tools
Requires:      net-tools
Requires:      openssh-clients
Requires:      psmisc
Requires:      python-unversioned-command
Requires:      python3
Requires:      python3-pexpect
Requires:      socat
Requires:      telnet
Requires:      which
Requires:      xterm

Provides:      mn(bin) = %{epoch}:%{version}-%{release}
Provides:      mnexec(bin) = %{epoch}:%{version}-%{release}

%description
Mininet creates a realistic virtual network, running real kernel, switch and application code, on a
single machine (VM, cloud or native), in seconds, with a single command.

%prep
%autosetup

%build
%set_build_flags
%make_build mnexec
%make_build mnexec.1
%make_build mn.1
%py3_build

%install
/usr/bin/make DESTDIR=%{buildroot} INSTALL="/usr/bin/install -p" \
 PREFIX=%{buildroot}%{_prefix} BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir} \
 install-mnexec
/usr/bin/make DESTDIR=%{buildroot} INSTALL="/usr/bin/install -p" \
 PREFIX=%{buildroot}%{_prefix} BINDIR=%{buildroot}%{_bindir} MANDIR=%{buildroot}%{_mandir} \
 install-manpages
%py3_install

%files
%{_bindir}/mn
%{_bindir}/mnexec
%{_mandir}/mn.1
%{_mandir}/mnexec.1
%{python3_sitelib}/mininet/
%{python3_sitelib}/mininet-*.egg-info/
%license LICENSE

%changelog
* Sun Dec 06 2020 Wojciech Kozlowski <wk@wojciechkozlowski.eu> 2.3.0d6
- Initial spec file
