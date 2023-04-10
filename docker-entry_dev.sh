#!/usr/bin/env bash

#check nodes are registered to the hub
url='http://localhost:4444/status'
status=$(curl --head --location --connect-timeout 5 --write-out %{http_code} --silent --output /dev/null ${url})
if [[ $status != 200 ]];
then
  echo sleeping;
  sleep 10;
fi;
# run py.test
pid="$!"
# selenium grid local run
pytest -s Python_excercices

#trap process id to stop script using Control+C
trap "echo '=== Stopping PID $pid ==='; kill -SIGTERM $pid" SIGINT SIGTERM

wait $pid