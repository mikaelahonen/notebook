import os
import csv

def main(opt):
	#Specify variables
	#</br> for html, \n for Linux, \r for Windows
	nl = opt['nl']
	delimiter = opt['delimiter']
	quote = opt['quote']
	#Optionally wrap file title and field name in html tags
	title_tag = opt['title_tag']
	field_tag = opt['field_tag']

	dir_read = input('Directory to read: ')
	#Current folder
	#dir_read = os.path.dirname(os.path.realpath(__file__))
	#Some other folder instead
	#dir_read = os.path.join("c:\\","path")

	#You can also set a custom directory to write instead
	dir_write = dir_read
	write_path = os.path.join(dir_write, 'headers.txt')
	#Open file for writing
	file_write = open(write_path,'w')

	#Loop files in directory
	for file in os.listdir(dir_read):

		#Get file name
		file_name = os.fsdecode(file)
		#Check that file ends with .csv
		if file.endswith(".csv"):
			#Get full path of the file
			read_path = os.path.join(dir_read, file_name)
			#Get full path of the file
			with open(read_path, newline='') as csv_file:
				csv_reader = csv.reader(csv_file, delimiter = delimiter, quotechar = quote)
				head_row = next(csv_reader)
				
				#Write filename
				title = wrapHtml(file_name, title_tag)
				file_write.write(title + nl)
				#Loop all heads in header row
				for head in head_row:
					head = wrapHtml(head, field_tag)
					file_write.write(head + nl)
					
				#Add space after all fields have been written
				file_write.write(nl + nl)
				
	file_write.close()
	print('Ready. Headers file: ' + write_path)

def wrapHtml(str, tag):
	
	#If tag is nothing, just return the original string
	if(tag == ''):
		return str
	else:
		tag_open = '<' + tag + '>'
		tag_close = '</' +  tag + '>'
		html = tag_open + str + tag_close
		return html
	
