#!/bin/sh

if [ $# != 0 ]
then
  outputFile='hh_positions_concatenated.csv'

  head -1 $1 > $outputFile

  for var in $@
  do
    tail -n +2 $var
  done | sort -n -t"," -k2.2,2.5 -k2.7,2.8 -k2.10,2.11 -k2.13,2.14 -k2.16,2.17 -k2.19,2.20 -k1.2,1.9 >> $outputFile

else
  echo 'Provide paths_to_csv_file as an argument!'
fi
