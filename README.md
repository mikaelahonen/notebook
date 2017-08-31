# Parse csv headers from multiple files

Python 3 code to parse headers from multiple files to list grouped by file name.

## Input files example
file-1.csv
```sh
first,last,age
John,Doe,25
Mary,Jane,25
Hello,World,42
```

file-2.csv
```sh
company,revenue,profit,profit margin
Consulting LTD,2 000 000,100 000,"5,0%" 
```

## Output file example
```sh
file-1.csv
first
last
age

file-2.csv
company
revenue
profit
profit margin
```

## Installation

Download the executable python file to your computer.

The only requirement is that you have Python 3 installed on you computer. Make sure you have python set to an environment variable.

## Preparation
Set options in `opt` array in `run.py`

New line character: </br> for html, \n for Linux, \r for Windows
```sh
opt['nl'] = '<br/>'
```
Csv delimiter
```sh
opt['delimiter'] = ';'
```
Csv quote character
```sh
opt['quote'] = '"'
```
Optionally wrap file title and field name in html tags. If you don't want this, leave it as empty string.
```sh
opt['title_tag'] = 'h2'
```
New line after title? If you use html tags you probably want to leave this to False.
```sh
opt['title_nl'] = False
```
Use this, if you want to weap field names to <p></p> tags for example.
```sh
opt['field_tag'] = ''
```
New line after a field row? If your field rows are wrapped around html tags, you probably want to leave this to False.
```sh
opt['title_nl'] = False
```
```sh
Number of new lines after each of the fields of a file have been listed
opt['trailing_nls'] = 2
```

## Usage
Open command line
Go the folder that includes the executable python script that you downloaded.
Run this
```sh
python run.py
```

The python script generates a `headers.txt` file to the same folder that you had the csv files.

## Background

I needed this script in a data warehouse project to document contents of some csv files.
