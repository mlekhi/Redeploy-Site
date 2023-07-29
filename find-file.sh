#!/bin/bash

MATCHES=($(find / -type f -name "$1"))
NUM_MATCHES=${#MATCHES[@]}

echo "Found $NUM_MATCHES matches"

for ((i = 0; i < NUM_MATCHES; i++));
do
        echo "${MATCHES[$i]}"
done
