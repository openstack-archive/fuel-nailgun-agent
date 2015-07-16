%define name nailgun-agent
%{!?version: %define version 7.0.0}
%{!?release: %define release 1}

Name:      %{name}
Version:   %{version}
Release:   %{release}
Source0:   %{name}-%{version}.tar.gz
Summary:   Nailgun startup agent
URL:       http://mirantis.com
License:   ASL 2.0
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Prefix:    %{_prefix}

Requires:  dmidecode
Requires:  ethtool
Requires:  rubygem-httpclient
Requires:  rubygem-ipaddress
Requires:  rubygem-json
Requires:  rubygem-ohai
Requires:  rubygem-rethtool
Requires:  rubygems

%description
The nailgun agent collects the server’s hardware information and submits it
to Nailgun through the REST API. Also it's responsible for reporting the
online/offline status and for initial setup Mcollective service.

%prep
%setup -cq -n %{name}-%{version}

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/cron.d

install -m 755 %{_builddir}/%{name}-%{version}/agent %{buildroot}/usr/bin/nailgun-agent
install -m 644 %{_builddir}/%{name}-%{version}/nailgun-agent.cron %{buildroot}/etc/cron.d/nailgun-agent

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/nailgun-agent
/etc/cron.d/nailgun-agent
