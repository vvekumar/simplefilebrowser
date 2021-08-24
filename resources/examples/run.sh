#!/bin/bash
#######################
# Run sfb-api using cURL
######################
USERNAME=calvin
PASSWORD=hobbes

# Run cURL to show contents of /tmp/wv (assumes already created)
ROOT_DIR=$MNT_LOC
RELPATH=

# save curl output to resp.json
curl -o resp.json -u ${USERNAME}:${PASSWORD} "0.0.0.0:5000/sfb/api?root=${ROOT_DIR}&relpath=${RELPATH}"
sleep 2
less resp.json | python -m json.tool

# show request URI info
echo "Showing request info: "
docker logs sfb-api 1>/dev/null 2> debug.log
tail -1 debug.log