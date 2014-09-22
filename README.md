SELinux policy module for the PostgreSQL install of the PGDG.

This modules adds the file contexts needed by the rpm of PostgreSQL
provided by the PGDG (e.g. yum.postgresql.org). It requires the
`postgresql` module of the ref policy.

Currently, it only has been tested with RHEL/Centos 6, using policy version 24.
It does not force you to enable sepgsql.

*Note:* when running the postmaster on a TCP port different than 5432, you
need to allow it to bind to the port y adding a `semanage port` rule to the
local policy.

This is free software distributed under the PostgreSQL license.

Copyright (c) 2014 Dalibo.
