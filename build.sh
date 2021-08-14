#!/bin/bash
######################################
# Build script to install dependencies
# and run integ tests
######################################

APP_NAME="sfb-api"
PATH_TO_DOCKER=`which docker`
echo ${PATH_TO_DOCKER}

# build
make install
pip install -r requirements.txt # [OPTIONAL] if running pytest locally

sleep 2
# verify
is_err=`py.test | egrep "== ERRORS =="`

if [[ -n ${is_err} ]]; then
  echo
  echo "**ERROR**"
  echo "WOOPS!! Looks like the build failed : either the deployment or integ test(s) failed. Run 'docker logs' for details"
  exit 1
else
  echo
  echo "SUCCESS!!"
fi