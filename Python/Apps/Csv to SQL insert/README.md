# Csv to SQL insert
I had data in an Excel file that I wanted to transfer to database server.
PostgreSQL PgAdmin wasn't able to read local file to remote database server.

So I decided to export Excel files in csv format and 
wrote this python script that reads the csv 
and creates SQL insert commands automatically.

From config file it is possible to set variables:
* The name of the table that you are inserting to.
* Parameters about how csv file should be read.
* Output format of SQL string. For example null and empty string parameters.

Tested with python 3.6.