#!/bin/bash

# This script makes create table scripts in SQL

files=`ls *.csv`


echo "USE RAN;"
echo
echo

# create drop if exists
for i in $files;
do
  tableName="${i%.*}"
  echo "DROP TABLE IF EXISTS $tableName;"
done

echo
echo

# generate create table queries
for i in $files;
do
  tableName="${i%.*}"

  #generate table query
  echo "CREATE TABLE $tableName ("
  tableAttr=`head -1 $i`
  DBattr=`echo $tableAttr | sed 's/,/ VARCHAR(100), /g'`

  #check if there is a rowID primary key
  PriKeyCheck=`echo $tableAttr | grep ".*RowID," | wc -c`

  # check if there is a rowID and set it as the Primary key
  if [[ $PriKeyCheck -ne 0 ]]
  then
    DBattr="$DBattr VARCHAR(100),"
    DBattr="$DBattr PRIMARY KEY (`echo $tableAttr | sed 's/,/ /g' | awk '{print $1}'`)"
  else
    DBattr="$DBattr VARCHAR(100)"
  fi

  echo $DBattr

  echo ");"
  echo
done

echo
echo

# generate csv loading queries
for i in $files;
do
  tableName="${i%.*}"
  echo "LOAD DATA INFILE './$i'"
  echo "INTO TABLE $tableName"
  echo "FIELDS TERMINATED BY ','"
  echo "LINES TERMINATED BY '\n'"
  echo "IGNORE 1 ROWS;"
  echo
done