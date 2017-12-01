# sql-examples
My notes for SQL.

## PostgreSQL

### Copy
Copy a file to the database. This example is for csv files.
For csv files `\N` is default for `null`.

`COPY table_name(col_1, col_2, col_3) FROM 'C:/Users/John Smith/folder/file.csv' DELIMITER ';' CSV HEADER;`

Example csv data
```
"col_1","col_2","col_3"
"Value 1","Other value","More text"
"Value 2","Another value","More text, yeaah!"
```
