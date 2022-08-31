#!/bin/sh

# id, created_at, name, has_test, alternate_url

if [ $# == 1 ]
then
  jsonFile=$1
else
  jsonFile="../ex00/hh.json"
fi

outputFile='hh.csv'
filterFile='filter.jq'

filters=$(<$filterFile)         # reading filters from file (cat isn't allowed in subject)
filters=${filters//, / }        # to remove extra commas and spaces

filtersJq=""
for i in $filters               # to make a string acceptable for jq
do
  if [ "$filtersJq" == "" ]
  then
    # putting into quotes so if we have filter with space it doesn't crash,
    # and it'll be easier to convert to the subject's style
    filtersJq=".\"$i\""
  else
    filtersJq+=",.\"$i\""
  fi
done
# converting a string with filter words to the one required by the subject (with quotes and commas)
# putting filters in csv file as 1 line
echo ${filtersJq//./} > $outputFile


len=`jq '.items | length' $jsonFile`
for (( i=0; i<$len; i++ ))
do
  # flag '-c' writes in one line by comma but if only we put a result in some brackets (didn't find out another way)
  # applying filters to items[i], removing brackets, writing to file
  tmp=`jq -c ".items | .[$i] | [$filtersJq]" $jsonFile`
  if [ "$tmp" != "" ]
  then
    echo ${tmp//[][]/} >> $outputFile
  fi
done
