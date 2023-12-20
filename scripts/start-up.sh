#!/bin/bash

function wait_for() {
  until ping -c 1 $1 > /dev/null; do
    echo "Waiting for $1 container..."
    sleep 3
  done
}

function clean_up() {
  rm -rf  alembic/ *.{ini,toml,lock,yml} 
}

case $APP in
  "helium")
      wait_for $WAIT_SERVICE
      alembic upgrade head
      gunicorn -w 4 'helium:app' -b 0.0.0.0:8000 --reload
    ;;
esac
