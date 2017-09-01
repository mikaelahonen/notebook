# Parse csv headers from multiple files

Python 3 code to parse headers from multiple csv files to generate field list of each file.
<br/>
Link to related blog post:
<br/>
[Blog post: Get csv headers (In English)](https://mikaelahonen.com/en/blog/csv-headers-list-using-python/)
<br/>
[Blog post: Get csv headers (In Finnish)](https://mikaelahonen.com/fi/blog/csv-tiedostojen-kentat-listaksi-pythonilla/)

## Input files example
`file-1.csv`
```sh
first,last,age
John,Doe,25
Mary,Jane,25
Hello,World,42
```

`file-2.csv`
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

Clone this github repository to your computer.

The only requirement is that you have Python 3 installed on you computer. The code has been tested only with Python 3.6.

## Preparation
Set options in `opt` array in `run.py` file of this repository.

New line characters
- `<br/>` for html
- `\n` for Linux
- `\r` for Windows
```python
opt['nl'] = '<br/>'
```
Csv delimiter
```python
opt['delimiter'] = ';'
```
Csv quote character
```python
opt['quote'] = '"'
```
Optionally wrap file title and field name in html tags such as `<h2></h2>`. If you don't want this, leave it as empty string.
```python
opt['title_tag'] = 'h2'
```
New line after title? If you use html tags you probably want to leave this to False.
```python
opt['title_nl'] = False
```
Use this, if you want to weap field names to `<p></p>` tags for example.
```python
opt['field_tag'] = ''
```
New line after a field row? If your field rows are wrapped around html tags, you probably want to leave this to False.
```python
opt['title_nl'] = False
```
Number of new lines after fields of a single file have been listed 
```python
opt['trailing_nls'] = 2
```

## Usage
Open the command line.
Go the folder that includes the `run.py` python script that you downloaded and run it.
Make sure you have python set to an environment variable - Otherwise you have to use the full path of your python installation.
```sh
python run.py
```
The script asks the location of the folder that you have your csv files.
```sh
Directory to read: C:\Users\mikael\Desktop\csv-folder
```

The python script generates a `headers.txt` file to the same folder that you had the csv files.

## Background

I needed this script in a data warehouse project to document contents of some csv files.
