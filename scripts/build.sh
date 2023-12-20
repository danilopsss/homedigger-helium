#!/bin/bash

function install_system_packages() {
  apt-get update -y
  apt-get install iputils-ping -y
}

function install_python_packages() {
  pip install --upgrade pip
  pip install poetry
  poetry config virtualenvs.create false

  if [ "$ENV" = "DEV" ]; then
    poetry install --no-root
  else
    poetry install --no-dev
  fi
}

case $APP in
  "helium")
      install_system_packages
      install_python_packages
    ;;
  *)
      install_system_packages
      install_python_packages
    ;;
esac
