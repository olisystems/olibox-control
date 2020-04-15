#! /bin/sh

[ -e "$SNAP_USER_DATA/config.toml" ] || touch $SNAP_USER_DATA/config.toml

[ -e "$SNAP_USER_DATA/data.json" ] || echo "{}" >> $SNAP_USER_DATA/data.json

cp $SNAP/ca-certificates.crt $SNAP_USER_DATA/ca-certificates.crt

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

exec "$@"