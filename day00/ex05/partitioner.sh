#!/bin/sh

if [ $# == 1 ]
then

  header=`head -1 $1`

  tail -n +2 $1 | awk 'BEGIN{FS="\",\""} {print $2}'  \
                | awk 'BEGIN{FS="T"} { print $1 }'    \
                | uniq                                \
                | awk -v var="$header" '{ print var > $1 }' # putting headers in new files

  tail -n +2 $1 | awk 'BEGIN{FS="\",\""}
                {
                  print $0 >> substr($2, 0, index($2, "T")-1)
                }'

else
  echo 'Provide 1 path_to_csv_file as an argument!'
fi
