# SELinux policy module for the PostgreSQL install of the PGDG

This modules adds the file contexts needed by the RPM of PostgreSQL
provided by the PGDG (e.g. yum.postgresql.org). It requires the
`postgresql` module of the ref policy, which is enabled by default.

## RedHat Version / Support

Version up to 1.2.0 support RHEL/Centos 6 (policy version 24)

As of 1.3.0, it supports RHEL/Centos 7 (policy version 31).

It does not force you to enable sepgsql.

## Boolean Provided

This policy provides a `postgresql_pgdg_can_http` similar to `postgresql_can_rsync`
from refpolicy. When enabled, this boolean allows PostgreSQL to use HTTP ports
in e.g. `archive_command`, `recovery_end_command`, etc.

``` console
# setsebool postgresql_pgdg_can_http on
# getsebool postgresql_pgdg_can_http
postgresql_pgdg_can_http --> on
#
```

Read/Write access to watchdog devices is provided by the
`postgresql_pgdg_use_watchdog` boolean. The purpose of this boolean is
to allow confining Patroni (a HA framework for PostgreSQL) with the
`postgresql_t` type. Patroni being in charge of running the
postmaster.

``` console
# setsebool postgresql_pgdg_use_watchdog on
# getsebool postgresql_pgdg_use_watchdog
postgresql_pgdg_use_watchdog --> on
#
```

## Notes

When running the postmaster on a TCP port different than 5432, you
need to allow it to bind to the port by adding a `semanage port` rule to the
local policy.

Appling `postgresql_t` to Patroni requires to :

* enable `postgresql_pgdg_can_http`
* label the DCS tcp port with `http_port_t` (tested with Etcd)
* use a unregistered port for the API of Patroni and label it with `postgresql_port_t`


# License

This is free software distributed under the PostgreSQL license.

Copyright (c) 2014-2020 Dalibo.
