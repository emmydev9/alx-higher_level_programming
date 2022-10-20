#!/bin/bash
# Script that sends a data with POST request
curl -Ls -X POST "$1" -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}'
