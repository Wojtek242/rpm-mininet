#!/usr/bin/env sh

SPEC_VERSION=`grep "Version:" mininet.spec | awk '{print $2}'`
REMOTE_VERSION=`git ls-remote --tags https://github.com/mininet/mininet.git | awk '{print $2}' | grep -E "refs/tags/[0-9]+.[0-9]+.[0-9]+" | sort --version-sort | tail -n 1 | cut -d '/' -f 3`

if [ "${SPEC_VERSION}" = "${REMOTE_VERSION}" ]
then
    echo "No new version : skipping update"
    exit 0
fi

echo "New version {${REMOTE_VERSION}} : updating"
sed -ri "s/(Version:\s+).*$/\1${REMOTE_VERSION}/" mininet.spec
