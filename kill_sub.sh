#!/bin/bash
for pid in $(lsof -t -i:"$1");
do
  sudo kill -9 "$pid";
done