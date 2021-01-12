#!/bin/bash

# Kills all running Docker containers

containers="$(docker ps -q)"
if [ -z "$containers" ]
then
  echo "No Docker containers to kill. Containers: $containers"
else 
  echo "Killing Docker containers: $containers"
  docker kill "$containers"
  sleep 5
fi
docker ps