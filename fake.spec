Summary:	Switches in redundant servers using arp spoofing
Name:		fake
Version:	1.1.11
Release:	3
License:	GPLv2+
Group:		Networking/Other
Url:		http://www.vergenet.net/linux/fake/
Source0:	http://www.vergenet.net/linux/fake/download/%{version}/%{name}-%{version}.tar.gz

%description
Fake is a utility that enables the IP address be taken over
by bringing up a second interface on the host machine and
using gratuitous arp. Designed to switch in backup servers
on a LAN.

%files
%defattr(644,root,root,755)
%doc COPYING AUTHORS README ChangeLog docs/* instance_config/* heartbeat/fake
%defattr(-,root,root)
%{_prefix}/sbin/*
%{_mandir}/man8/*
%dir %{_sysconfdir}/fake
%config(noreplace) %{_sysconfdir}/fake/instance_config
%config(noreplace) %{_sysconfdir}/fake/.fakerc
%config(noreplace) %{_sysconfdir}/fake/clear_routers
%{_prefix}/lib/heartbeat/fake

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%make patch
%make CC="gcc %{optflags}"

%install
make ROOT_DIR=%{buildroot} MAN8_DIR=%{buildroot}%{_mandir}/man8 install
rm -rf %{buildroot}%{_prefix}/doc/

