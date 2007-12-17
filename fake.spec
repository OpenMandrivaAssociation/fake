%define	name	fake
%define	version	1.1.10
%define rel	3
%define	release	%mkrel %{rel}

Summary: 	Switches in redundant servers using arp spoofing
Name: 		%{name}
Version:	%{version}
Release:	%{release}
license:	GPL
Group:		Networking/Other
Source0:	http://www.vergenet.net/linux/fake/download/%{version}/%{name}-%{version}.tar.bz2
URL:		http://www.vergenet.net/linux/fake/

%description
Fake is a utility that enables the IP address be taken over
by bringing up a second interface on the host machine and
using gratuitous arp. Designed to switch in backup servers
on a LAN.

%prep
%setup -q

%build
%make patch
%make CC="gcc $RPM_OPT_FLAGS -s"

%install
rm -rf $RPM_BUILD_ROOT

make ROOT_DIR=$RPM_BUILD_ROOT MAN8_DIR=$RPM_BUILD_ROOT%{_mandir}/man8 install
rm -rf $RPM_BUILD_ROOT/usr/doc/

%clean
rm -rf $RPM_BUILD_ROOT

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
