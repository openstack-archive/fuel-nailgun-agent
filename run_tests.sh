#!/bin/bash
# RVM

set -ex

function cd_workspace() {
  cd $(dirname $(readlink -f $0)) > /dev/null
}

function ruby_checks() {
  cd_workspace

  ruby -wc agent
}

ruby_checks $@
