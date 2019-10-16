#!/bin/bash -eux

teardown() {
    exit_code=$?
    trap - EXIT INT TERM
    chown -R $(stat -c %u:%g $0) *

    # Ease debugging from Docker container by waiting for explicit shutdown.
    if [ -z "${CI-}" -a $$ -eq 1 -a $exit_code -gt 0 ] ; then
        tail -f /dev/null
    fi
}

trap teardown EXIT INT TERM

rpmname=selinux-policy-pgsql-pgdg
srcdir=$(readlink -m $0/..)
cd $srcdir

chown -R $(id -nu):$(id -ng) selinux* postgresql-pgdg* README.md

topdir=${PWD}/rpm
mkdir -p $topdir

sudo yum install -y rpmlint
sudo yum-builddep -y $rpmname.spec
rpmbuild -ba \
    --define "_topdir ${topdir}" \
    --define "_sourcedir ${srcdir}" \
    $rpmname.spec

rpm=rpm/noarch/$rpmname-*.noarch.rpm
rpmlint $rpm

# Test it
if rpm -q $rpmname >/dev/null ; then
    sudo yum remove -y $rpmname
fi
sudo yum install -y $rpm
sudo semodule -l | grep postgresql-pgdg
