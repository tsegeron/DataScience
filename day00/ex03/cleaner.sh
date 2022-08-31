#!/bin/sh

if [ $# == 1 ]
then
  csvFile=$1
else
  csvFile="../ex02/hh_sorted.csv"
fi


outputFile='hh_positions.csv'

head -1 $csvFile > $outputFile

tail -n +2 $csvFile | awk 'BEGIN{FS=OFS="\","}
{

positions=""

if (index(tolower($3), "junior") != 0) positions=positions"Junior/"
if (index(tolower($3), "middle") != 0) positions=positions"Middle/"
if (index(tolower($3), "senior") != 0) positions=positions"Senior"
if (positions == "") positions="-"

gsub(/\/$/, "", positions)

$3="\""positions
print
}' >> $outputFile
