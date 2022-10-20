#!/bin/bash
# Script that load a data from a file
curl -s -X POST "$1" -d "@$2" -H "Content-Type: application/json"
