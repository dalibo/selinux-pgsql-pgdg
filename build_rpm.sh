#!/bin/sh

# clean
rm $HOME/rpmbuild/BUILD/postgresql-pgdg.*
rm $HOME/rpmbuild/SRPMS/selinux-policy-pgsql-pgdg-*.src.rpm
rm $HOME/rpmbuild/RPMS/x86_64/selinux-policy-pgsql-pgdg-*.x86_64.rpm
rm $HOME/rpmbuild/SOURCES/postgresql-pgdg.{if,te,fc}

# Copy sources
mkdir -p $HOME/rpmbuild/BUILD
mkdir -p $HOME/rpmbuild/SOURCES
for x in if te fc; do
    cp `dirname $0`/postgresql-pgdg.$x $HOME/rpmbuild/SOURCES
done

# build
rpmbuild -ba `dirname $0`/selinux-policy-pgsql-pgdg.spec
