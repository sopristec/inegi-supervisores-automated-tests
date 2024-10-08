#!/bin/bash

# Check if a parameter is passed
if [ -z "$1" ]; then
  echo "Please provide the name of the JSON file."
  exit 1
fi

cd /home/ltaas/inegi-supervisores-automated-tests
source .venv/bin/activate 
nohup env PYTHONUNBUFFERED=1 python coordinator_async.py entrevistas "feeder_entrevistas/$1" >> /home/ltaas/inegi-supervisores-automated-tests/entrevistas_cron.log 2>&1 &