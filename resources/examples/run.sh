#!/bin/bash
#######################
# Run sfb-api using cURL
######################
USERNAME=calvin
PASSWORD=hobbes

# Run cURL to show contents of /tmp/wv (assumes already created)
ROOT_DIR=/tmp
RELPATH=/wv

# save curl output to resp.json
curl -o resp.json -u ${USERNAME}:${PASSWORD} 0.0.0.0:5000/sfb/api?root=${ROOT_DIR}&relpath=${RELPATH}

less resp.json | python -m json.tool