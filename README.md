# Parse csv headers from multiple files

Python 3 code to parse headers from multiple files to list grouped by file name.

## Installation

Download the executable python file to your computer.

The only requirement is that you have Python 3 installed on you computer. Make sure you have python set to an environment variable.

## Preparation
Set options in opt array in run.py

#Specify variables
</br> for html, \n for Linux, \r for Windows
```sh
opt['nl'] = '<br/>'
```

```sh
opt['delimiter'] = ';'
```
opt['quote'] = '"'

Optionally wrap file title and field name in html tags
```sh
opt['title_tag'] = 'h2'
```
#New line after title?
opt['title_nl'] = False
opt['field_tag'] = ''

## Usage
Open command line
Go the folder that includes the executable python script that you downloaded.
Run this
```sh
python run.py
```

The python script generates a text headers.txt file to the same folder that you execute run.py from.

## Background

I needed this script in a data warehouse project. 
I needed to parse headers from csv transfer files for documentation purposes.
