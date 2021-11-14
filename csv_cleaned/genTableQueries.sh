#!/bin/bash

files=`ls *.csv`

echo $files

for i in $files;
do
  echo "CREATE TABLE $i ("
  head -1 $i | sed 's/,/ VARCHAR(100), /g'
done

echo " VARCHAR(100))"