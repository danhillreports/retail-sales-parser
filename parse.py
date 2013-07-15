import csv

extensions_dict = [{u'Furniture and Home Furnishings Stores': u'adv44200.txt'}, 
	{u'Food Services and Drinking Places': u'adv72200.txt'}, 
	{u'General Merchandise Stores': u'adv45200.txt'}, 
	{u'Motor Vehicle and Parts Dealers': u'adv44100.txt'}, 
	{u'Building Material and Garden Equipment and Supplies Dealers': u'adv44400.txt'}, 
	{u'Miscellaneous Store Retailers': u'adv45300.txt'}, 
	{u'Retail and Food Services Total': u'adv44x72.txt'}, 
	{u'Health and Personal Care Stores': u'adv44600.txt'}, 
	{u'Food and Beverage Stores': u'adv44500.txt'}, {u'Gasoline Stations': u'adv44700.txt'}, 
	{u'Clothing and Clothing Accessories Stores': u'adv44800.txt'}, 
	{u'Sporting Goods, Hobby, Book, and Music Stores': u'adv45100.txt'}, 
	{u'Electronics and Appliance Stores': u'adv44300.txt'},
	{u'Nonstore Retailers': u'adv45400.txt'}, {u'Retail and Food Services Total': u'adv44x72.txt'}]

for extension in extensions_dict:

	write_file = 'csv/' + extension.keys()[0] + '.csv'
	read_file = 'txt/' +extension.values()[0]
	reader = list(csv.reader(open(read_file, 'rb'), delimiter='\t'))

	writer=csv.writer(open(write_file, 'wb'), quoting=csv.QUOTE_MINIMAL)

	heads = ['YEAR', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
	YEAR, JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC = range(0,13) # goofy initialization
	heads_vars = [YEAR, JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC]

	writer.writerow(heads)
	i=0
	print write_file
	for row in reader:
		for cell in row:
			i=i+1
			if i > 2 and i < 25:
				if write_file == 'csv/Retail and Food Services Total.csv': # always be huntin edge cases
					cell = cell.split('   ')
				else:
					cell = cell.split('    ')

				# these columns get one less space...
				year = cell[0]
				jan = cell[1]
				
				# ... so we trim these columns
				for index in range(2,13):
					heads_vars[index] = cell[index][1:]
				writer.writerow([year, jan, heads_vars[2], heads_vars[3], heads_vars[4], heads_vars[5], heads_vars[6], heads_vars[7],
					heads_vars[8], heads_vars[9], heads_vars[10], heads_vars[11], heads_vars[12]])