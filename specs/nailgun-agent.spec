%define name nailgun-agent
%{!?version: %define version 7.0.0}
%{!?release: %define release 1}

Summary:   Nailgun startup agent
Version:   %{version}
Release:   %{release}
License:   ASL 2.0
BuildRoot: %{_tmppath}/%{name}-%{version}
URL:       http://mirantis.com
Requires:  rubygem-rethtool
Requires:  rubygem-ohai
Requires:  rubygem-httpclient
Requires:  rubygem-ipaddress
Requires:  rubygem-json
Requires:  rubygems
Requires:  ethtool

%description
Nailgun startup agent that register node at Nailgun and make a little setup
of other services.

%prep
%setup -cq -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt/nailgun/bin
mkdir -p %{buildroot}/etc/cron.d

install -m 755 %{_builddir}/%{name}-%{version}/agent %{buildroot}/opt/nailgun/bin/agent
install -m 644 %{_builddir}/%{name}-%{version}/nailgun-agent.cron %{buildroot}/etc/cron.d/nailgun-agent

%clean
rm -rf $RPM_BUILD_ROOT

%files
/opt/nailgun/bin/agent
/etc/cron.d/nailgun-agent
