#!/bin/bash

if [ -z "$1" ]
  then
    echo "Usage: $0 <service name>"
    exit 1
fi

sudo systemctl restart "$1"

