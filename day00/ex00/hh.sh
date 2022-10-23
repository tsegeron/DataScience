#!/bin/bash


if [ $# == 1 ]
then
  outputFile='hh.json'
  vacancy=""

  for i in $1
  do
    if [ "$vacancy" == "" ]
    then
      vacancy=$i
    else
      vacancy+="+$i"
    fi
  done

  params="?text=$vacancy&page=0&per_page=20"
  URL="https://api.hh.ru/vacancies$params"

  curl --progress-bar -k -H 'User-Agent: api-test-agent' $URL | jq '.' > $outputFile
  echo "Done! Check results in file $outputFile"

else
  echo 'Provide 1 string as an argument!'
fi
