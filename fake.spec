%define	name	fake
%define	version	1.1.11
%define rel	2
%define	release	%mkrel %{rel}

Summary: 	Switches in redundant servers using arp spoofing
Name: 		%{name}
Version:	%{version}
Release:	%{release}
license:	GPL
Group:		Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}
Source0:	http://www.vergenet.net/linux/fake/download/%{version}/%{name}-%{version}.tar.gz
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


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.11-2mdv2011.0
+ Revision: 610418
- rebuild

* Wed Jan 27 2010 Antoine Ginies <aginies@mandriva.com> 1.1.11-1mdv2010.1
+ Revision: 497155
- add buildroot tag
- upload the tarball
- release 1.1.11

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.1.10-4mdv2010.0
+ Revision: 437511
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1.10-3mdv2008.1
+ Revision: 136408
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 22 2007 Antoine Ginies <aginies@mandriva.com> 1.1.10-3mdv2008.0
+ Revision: 29749
- Import fake



* Mon Aug  7 2006 Antoine Ginies <aginies@mandriva.com> 1.1.10-3mdv2007.0
- rebuild

* Fri May 06 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.1.10-2mdk
- lib64 fix
- fix ownerless dir
- %%mkrel
- compile with optimizations

* Sun Jul 25 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.1.10-1mdk
- 1.1.10
- fix doc permissions
- drop useless obsoletes (no reason to obsolete it self)
- quiet setup
- cosmetics

* Mon May 17 2004 Antoine Ginies <aginies@n2.mandrakesoft.com> 1.1.8-4mdk
- rebuild

* Mon Aug 18 2003 Antoine Ginies <aginies@bi.mandrakesoft.com> 1.1.8-3mdk
- rebuild 9.2

* Thu Feb 27 2003 Antoine Ginies <aginies@mandrakesoft.com> 1.1.8-2mdk
- rebuild
* Tue Jan 07 2003 Clic-dev <clic-dev-public@mandrakesoft.com> 1.1.8-1mdk
- based on Horms <horms@verge.net.au> spec file
- first release for Mandrakesoft
