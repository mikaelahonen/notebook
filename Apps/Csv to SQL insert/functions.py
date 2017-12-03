# Import pandas. Remember to install it first to your machine.
import os
import config
import csv

#Format row values with quotes and nulls if needed
def formatValue(value, col):
	
	#Is string empty or not?
	is_empty = value == ""
	
	#Pass parameter to new mutable variable
	new_value = value	
	
	#Value is empty
	if(is_empty):
		#Empty and quote
		if(config.fields[col]['quote_empty']):
			new_value = "''"
		#Empty and set to null
		else:
			new_value = 'null'
	#Value is not empty and quotes are wanted
	elif(not is_empty and config.fields[col]['quote']):
		new_value = "'" + new_value + "'"
		
	return new_value

#
def main():

	#Open csv file
	with open(config.file) as csv_file:

		#Read csv
		reader = csv.reader(
			csv_file, 
			delimiter = config.delim, 
			quotechar = config.quote
		)
		
		#Get header and make it SQL string
		header_list = next(reader)
		header_str = ','.join(header_list)
		
		#Initiate list for rows
		row_list = []
		
		#Loop all rows
		for row in reader:
			values = []
			
			#Loop all columns
			col = 0
			for value in row:
				value_str = formatValue(value, col)
				values.append(value_str)
				col += 1
				
			#Add the row to the list
			row_list.append('(' + ','.join(values) + ')')
			
		#Row list to string
		rows_str = ',\n'.join(row_list)
		
	#Print results
	print('INSERT INTO ' + config.table + '(' + header_str + ') VALUES ' + rows_str)
