import os

opt = {
	'path': 'C:/users/user/folder',
	'extension': '.html',
	'match_str': 'match this'
}

#Loop files in directory
for file in os.listdir(opt['path']):

	file_name = os.fsdecode(file)
	full_path = os.path.join(opt['path'], file_name)

	#Check that file ends with file extension
	if file.endswith(opt['extension']):

		#Open for reading
		with open(full_path, 'r') as f:
			#Get file contents
			content = f.read()
			#Match the string
			match = content.find(opt['match_str'])

			#If match was found
			if(match > 0):
				#Print file name
				print(file_name + '(' + str(match) + ')')
