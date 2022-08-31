#!/bin/sh

if [ $# == 1 ]
then
  csvFile=$1
else
  csvFile="../ex01/hh.csv"
fi


outputFile='hh_sorted.csv'

head -1 $csvFile > $outputFile

# sorting ignores timezone (-k2.22,2.25);
# -n for nums, -t for separating, -k for defining a range to sort
#                                     year      month       day       hour        minute      second      id
tail -n +2 $csvFile | sort -n -t"," -k2.2,2.5 -k2.7,2.8 -k2.10,2.11 -k2.13,2.14 -k2.16,2.17 -k2.19,2.20 -k1.2,1.9 >> $outputFile
