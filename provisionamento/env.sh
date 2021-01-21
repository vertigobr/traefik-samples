#!/bin/bash
#
# Use to set DOCKER env vars. Source from your .bashrc or .profile to set
# variable values on login.
#
export DOCKER_TLS_VERIFY=1
#export DOCKER_HOST="tcp://manager.vtg:2376"
export DOCKER_HOST="tcp://$(python terraform.py --debug --list | jq -r .managers.hosts[0]):2376"
export DOCKER_CERT_PATH=$(pwd)/certs
