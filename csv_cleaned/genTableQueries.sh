#!/bin/bash

files=`ls *.csv`

# echo $files

for i in $files;
do
  tableName="${i%.*}"
  echo "CREATE TABLE $tableName ("
  attr=`head -1 $i | sed 's/,/ VARCHAR(100), /g'`
  attr="$attr VARCHAR(100)"
  echo $attr
  echo ")"
  echo ""
done