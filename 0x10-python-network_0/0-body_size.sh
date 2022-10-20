#!/bin/bash
# Script to determine the size of a http response using curl
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
