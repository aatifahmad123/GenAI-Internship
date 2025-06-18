#!/bin/bash

for i in {1..5}; do
  for j in {1..10}; do
    echo "Running: python gcloudRequestAndMerge.py $i $j"
    python gcloudRequestAndMerge.py $i $j
  done
done
echo "All tasks completed."