#!/bin/sh

if [ $# == 1 ]
then
  csvFile=$1
else
  csvFile="../ex03/hh_positions.csv"
fi

outputFile='hh_uniq_positions.csv'

head -1 $csvFile | awk 'BEGIN { FS=",";ORS=",\"count\"\n"}; { print $3 }' > $outputFile

tail -n +2 $csvFile | awk 'BEGIN{FS=OFS="\",";countJ=0;countM=0;countS=0;}
{
  if (index(tolower($3), "junior") != 0) countJ++
  if (index(tolower($3), "middle") != 0) countM++
  if (index(tolower($3), "senior") != 0) countS++
}
END {
print "\"Junior\"," countJ
print "\"Middle\"," countM
print "\"Senior\"," countS
}' | sort -nr -t"," -k2 >> $outputFile
