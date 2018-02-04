import os

opt = {
	'path': 'C:/a/b/c',
	'extension': '.csv',
	'output_name': 'merged_csv.csv'
}

#Prepare file to write
write_path = os.path.join(opt['path'], opt['output_name'])
write_file = open(write_path,'w')

file_count = 0

#Loop files in directory
for file_read in os.listdir(opt['path']):



	read_file_name = os.fsdecode(file_read)
	read_path = os.path.join(opt['path'], read_file_name)

	#Check that file ends with file extension
	bool_1 = file_read.endswith(opt['extension'])
	bool_2 = file_read != opt['output_name']


	if bool_1 and bool_2:
		file_count += 1
		#Open for reading
		with open(read_path, 'r') as f:
			#Get file contents
			lines = f.readlines()

			line_count = 0

			for line in lines:
				write_file.write(line)
				line_count += 1

			write_file.write('\n')

		print(read_file_name + ': ' + str(line_count))

print("File count: " + str(file_count))
