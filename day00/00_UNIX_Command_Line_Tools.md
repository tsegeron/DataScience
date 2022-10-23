# UNIX Command Line Tools
*Using UNIX command-line tools for basic data science tasks.
Using `curl`, `sort`, `uniq`, `jq`, `sed`, and `cat` for data collection and preprocessing*


## Tasks
Check the [subject](en.subject.pdf) for more info
1. ex00 – Interacting with the [HeadHunter API](https://dev.hh.ru/) to parse some information about vacancies.\
   Shell script: 
   - gets the name of a vacancy as an argument (i.e. `‘data scientist’`)
   - downloads information about the first 20 vacancies
   - stores it in a file with the name `hh.json`
   >    The result in the file must be formatted in such a way that each field is placed on a
   different line. 
2. ex01 – Transforming JSON to CSV.\
   Shell script:
   - executes `jq` with a filter written in a separate file `filter.jq`
   - filters the following columns corresponding to the vacancies
   - saves the result to the CSV file `hh.csv`
   >    The CSV file must have headers in the first row
3. ex02 – Sorting a file.\
   Shell script:
   - sorts the `hh.csv` file from the previous exercise according to the columns `created_at`, `id` in ascending order
   - saves the result in the CSV file `hh_sorted.csv`
   >    The CSV file must have headers in the first row
4. ex03 – Data cleaning.\
   Shell script:
   - replaces text in the `name` column with Junior/Middle/Senior, depending on what is written there; replaces with `-`, if no record is present
   - saves the result in the CSV file `hh_positions.csv`
5. ex04 – Descriptive statistics.\
   Shell script:
   - counts unique values of the name column in the `hh_positions.csv`
   - sorts the table by that count in descending order
   - stores the result in the CSV file `hh_uniq_positions.csv`
6. ex05 – Partitioning and concatenation.\
   1. Shell script `partitioner.sh`:
      - takes as input `hh_positions.csv` (the result of Exercise 03)
      - stores slices of data with different `created_at` dates in separate CSV files named for that date
   2. Shell script `concatenator.sh`:
      - takes as input the separate files (i.e. the result of `partitioner.sh`)
      - concatenates all separate files into one CSV file
      > The CSV files must have headers in the first row. The data should be sorted by `created_at`, `id` in ascending order
