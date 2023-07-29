#!/bin/bash

RUNS=0
FILE=$1
TEST=true

until [[ "$?" -ne 0 ]];
  do
  ((RUNS++))
  $FILE &> out.txt 2> err.txt
done

echo "It took $RUNS runs to fail."
echo "Standard Output: "
cat out.txt
echo "Standard Error: "
cat err.txt

