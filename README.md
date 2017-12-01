# SQL Examples
My notes for SQL.

## PostgreSQL

### Copy
Copy a file to a database. This example is for csv files.
For csv files an unquoted empty string is default for `null`.
This doesn't work for transferring file from local PC to remote database server at least with PgAdmin.

`COPY table_name(col_1, col_2, col_3) FROM 'C:/Users/John Smith/folder/file.csv' DELIMITER ';' CSV HEADER;`

Example csv data
```
"col_1";"col_2";"col_3"
"Value 1";"Other value";"More text"
"Value 2";;"Previous value is null."
```
