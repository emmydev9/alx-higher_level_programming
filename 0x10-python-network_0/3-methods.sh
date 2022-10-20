#!/bin/bash
# script that list the supported http method on a server
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
