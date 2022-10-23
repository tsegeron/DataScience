# SQL
*SQL and Pandas.*

## Tasks
1. ex00 – Select
   - get the subtable from `pageviews` table using only one query where:
     - only `uid` and `datetime` are used
     - only user data (`user_*`) is used and not `admin` data
     - it is sorted by `uid` in *ascending* order
     - the *index column* is `datetime`
     - `datetime` is *converted* to `DatetimeIndex`
     - the *name of the dataframe* is `pageviews`
2. ex01 – Subquery
   - count the rows from the `pageviews` table but only with users from the `checker` table with:
     - `status = ’ready’`, we do not want to analyze the logs that are in status checking 
     - `numTrials = 1`, we want to analyze only the first commits, because only they can tell us when a student started working on a lab 
     - `labnames` should be from the list: `laba04`, `laba04s`, `laba05`, `laba06`, `laba06s`, `project1`. Only they were active during the experiment
3. ex02 – Join
   - create a new table `datamart` in the database by joining the tables `pageviews` and
`checker` using only one query
     - the table should have the following columns: `uid`, `labname`, `first_commit_ts`, `first_view_ts`
     - `first_commit_ts` is just a new name of the column `timestamp` from the `checker`
     table, it shows the first commit from a particular lab and from a particular
     user
     - `first_view_ts` is the first visit of a user to the table `pageviews`, `timestamp`
     when a user visited the newsfeed
     - `status = ’ready’` should still be a filter
     - `numTrials = 1` should still be a filter
     - `labnames` should be from the list: `laba04`, `laba04s`, `laba05`, `laba06`, `laba06s`, `project1`.
     - the table should contain only the users (uids with `user_*`) and not the `admin`s
     - `first_commit_ts` and `first_view_ts` should be parsed as `datetime64`
   - using Pandas methods, create two dataframes: `test` and `control`
     - `test` should have the users that have the values in `first_view_ts`
     - `control` should have the users that have missing values in `first_view_ts`
     - replace the missing values in the `control` with the *average* `first_view_ts` of the
     `test` users, we will use this value for the future analysis
     - save both tables into the database, you will use them in the next exercises
4. ex03 – Aggregations
   - Check the [subject](en.subject.pdf) for the task
5. ex04 – A/B-testing
   - Check the [subject](en.subject.pdf) for the task
