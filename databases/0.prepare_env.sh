#!/usr/bin/env bash

if [ "$(uname)" == "Darwin" ]; then
  brew install mysql
  export PATH=$PATH:/usr/local/mysql/bin
  pip install MySQL-Python
  brew install docker
  brew install boot2docker
  boot2docker init
  boot2docker up
  eval "$(boot2docker shellinit)"
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  sudo apt-get install libmysqlclient-dev
  sudo apt-get install mysql-client
  sudo apt-get -y install docker.io
  export PATH=$PATH:/usr/local/mysql/bin
  pip install MySQL-Python
fi
