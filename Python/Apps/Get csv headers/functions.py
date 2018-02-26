import os
import csv
#Configuration file
import config

def main():

	dir_read = input('Directory to read: ')

	#You can also set a custom directory to write instead
	if(config.write_dir is None):
		write_dir = dir_read
	else:
		write_dir = config.write_dir
	
	write_path = os.path.join(write_dir, 'headers.txt')
	#Open file for writing
	file_write = open(write_path,'w')

	#Loop files in directory
	for file in os.listdir(dir_read):

		#Get current file name
		file_name = os.fsdecode(file)
		
		#Check that file ends with .csv
		if file.endswith(".csv"):
		
			#Get full path of the file
			read_path = os.path.join(dir_read, file_name)
			
			#Get full path of the file
			with open(read_path, newline='') as csv_file:
				csv_reader = csv.reader(
					csv_file, 
					delimiter = config.delim, 
					quotechar = config.quote
				)
				
				#Get header
				head_row = next(csv_reader)
				
				#Write filename
				title = wrapHtml(file_name, config.title_tag)
				if(config.title_nl):
					file_write.write(title + config.nl)
				else:
					file_write.write(title)
					
				#Loop all heads in header row
				for head in head_row:
					head = wrapHtml(head, config.field_tag)
					if(config.field_nl):
						file_write.write(head + config.nl)
					else:
						file_write.write(head)
					
				#Add space after all fields have been written
				file_write.write(config.nl * config.trailing_nls)
				
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
	
