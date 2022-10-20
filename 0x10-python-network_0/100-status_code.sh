#!/bin/bash
# Script that display on the status code of a http response
curl -so /dev/null -w "%{http_code}" "$1"
