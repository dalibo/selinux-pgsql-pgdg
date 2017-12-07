%global selinux_variants targeted
%global selinux_policyver 3.7.19
%global modulename postgresql-pgdg
%global relabelpath /usr/pgsql-*/*

Name: selinux-policy-pgsql-pgdg
Version: 1.1.0
Release: 1
Summary: SELinux policy module for PostgreSQL from the PGDG
License: PostgreSQL
Group: System Environment/Base
Url: http://github.com/dalibo/selinux-pgsql-pgdg

Source1: %{modulename}.if
Source2: %{modulename}.te
Source3: %{modulename}.fc
Source4: README.md

BuildArch: noarch
BuildRequires: make
BuildRequires: selinux-policy-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: selinux-policy >= %{selinux_policyver}
Requires: selinux-policy-targeted
Requires(post):   /usr/sbin/semodule, /sbin/restorecon
Requires(postun): /usr/sbin/semodule, /sbin/restorecon

%description
SELinux policy module for PostgreSQL packages provided by the
PGDG. This module adds the file contexts needed to confine a
PostgreSQL cluster.

%prep
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} %{SOURCE4} ./

%build
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv %{modulename}.pp %{modulename}.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done

%install
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 %{modulename}.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp
done

%clean
rm -rf %{buildroot}

%post
for selinuxvariant in %{selinux_variants}
do
    /usr/sbin/semodule -s ${selinuxvariant} -u \
	%{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp &> /dev/null || :
done
if readlink -e %{relabelpath} &>/dev/null ; then
  /sbin/restorecon -R /etc/rc.d/init.d/ ${relabelpath} || :
fi

%postun
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
     /usr/sbin/semodule -s ${selinuxvariant} -r %{modulename} &> /dev/null || :
  done
  if readlink -e %{relabelpath} &>/dev/null ; then
    /sbin/restorecon -R /etc/rc.d/init.d/ ${relabelpath} || :
  fi
fi

%files
%defattr(-,root,root,0755)
%{_datadir}/selinux/*/%{modulename}.pp
%doc README.md

%changelog
* Mon Oct 23 2017 Nicolas Thauvin <nicolas.thauvin@dalibo.com> 1.1.0-1
- support PostgreSQL 10

* Mon Jan 28 2015 Nicolas Thauvin <nicolas.thauvin@dalibo.com> 1.0.1-1
- Follow the selinux module revision bump for proper rpm update

* Mon Jan 23 2015 Marcus Berglof <marcus.berglof@gmail.com> 1.0.0-2
- Added postgresql_log_t for pgstartup.log and pg_log

* Mon Sep 22 2014 Nicolas Thauvin <nicolas.thauvin@dalibo.com> 1.0.0-1
- Initial version

