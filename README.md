# SELinux policy module for the PostgreSQL install of the PGDG

This modules adds the file contexts needed by the RPM of PostgreSQL
provided by the PGDG (e.g. yum.postgresql.org). It requires the
`postgresql` module of the ref policy.

Currently, it only has been tested with RHEL/Centos 6, using policy version 24.
It does not force you to enable sepgsql.

*Note:* when running the postmaster on a TCP port different than 5432, you
need to allow it to bind to the port by adding a `semanage port` rule to the
local policy.

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

This is free software distributed under the PostgreSQL license.

Copyright (c) 2014-2019 Dalibo.
