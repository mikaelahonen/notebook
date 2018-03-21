# SQL Examples
My notes for SQL.

## PostgreSQL

### Copy data from file
Copy a file to a database. This example is for csv files.
For csv files an unquoted empty string is default for `null`.
This doesn't work for transferring file from local PC to remote database server at least with PgAdmin.

`COPY table_name(col_1, col_2, col_3) FROM 'C:/Users/John Smith/folder/file.csv' DELIMITER ';' CSV HEADER;`

Example csv data
```sql
"col_1";"col_2";"col_3"
"Value 1";"Other value";"More text"
"Value 2";;"Previous value is null."
```

### Insert into multiple values
```sql
INSERT INTO table_name(col_1, col_2, col_3)
VALUES
(0, false, "text"),
(4, true, "more text")
```

### Case insensitive wild card match
By default `like` statement results are case sensitive.
To make `like` case insensitive use this:
```sql
SELECT *
FROM table_name
WHERE LOWER(column_1) LIKE '%text_to_match%'
```

## SQL server

### Lag
```sql
select *, LAG(col_1, 1) OVER (ORDER BY col_1) as col_1_prev
from table_name
```
Note: Lag can be used with partition as well.
