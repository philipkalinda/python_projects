results = []
credits = []
classified_results = []

msc_classification = {
	'Distinction':{
		'min': 69.5,
		'max': 100},
	'Merit':{
		'min': 59.5,
		'max': 69.5},
	'Pass':{
		'min': 49.5,
		'max': 59.5},
	'Fail':{
		'min': 0,
		'max': 49.5}
}

bsc_classification = {
	'1st':{
		'min': 69.5,
		'max': 100},
	'2.1':{
		'min': 59.5,
		'max': 69.5},
	'2.2':{
		'min': 49.5,
		'max': 59.5},
	'3rd':{
		'min': 39.5,
		'max': 49.5},
	'Fail':{
		'min': 0,
		'max': 39.5}
}


print('this calculates your overall result from all your module results\n')
while True:
	deg_type = input('are you studying an \'msc\' or a \'bsc\'?\n> ')
	if deg_type == 'msc' or deg_type== 'bsc':
		break
	else:
		print('please enter \'bsc\' or \'msc\' ')

while True:
	print('When finished, please enter \'done\'')
	result = input('please enter your result\n> ')
	try:
		if result == 'done':
			break
		result = int(result)
	except ValueError:
		print('the \'result\' you entered is not an integer. please enter an integer')
	
	credit = input('please enter how many credits the result is worth\n> ')
	try:
		if result == 'done':
			break
		credit = int(credit)
	except ValueError:
		print('the \'credits\' you entered is not an integer. please enter an integer')
	results.append(result)
	credits.append(credit)

final_grade = (sum([results[indx]*credits[indx] for indx in range(0,len(results))]) / sum([100*cred for cred in credits]))*100

if deg_type=='msc':
	for key, grade in msc_classification.items():
		if final_grade < grade['max'] and final_grade > grade['min']:
			print('\nYour final grade is {} at {}%'.format(key, (int(final_grade))))
		else:
			continue
	for result_ in results:
		for key, grade in msc_classification.items():
			if result_ < grade['max'] and result_ > grade['min']:
				classified_results.append(key)
	print('\nYour individual grades are as follows:')
	for idx in range(0, len(classified_results)):
		print('{} - {} - {} Credits'.format(results[idx], classified_results[idx],credits[idx]))

if deg_type=='bsc':
	for key, grade in bsc_classification.items():
		if final_grade < grade['max'] and final_grade > grade['min']:
			print('\nYour final grade is a {} at {}%'.format(key, (int(final_grade))))
		else:
			continue
	for result_ in results:
		for key, grade in bsc_classification.items():
			if result_ < grade['max'] and result_ > grade['min']:
				classified_results.append(key)
	print('\nYour individual grades are as follows:')
	for idx in range(0, len(classified_results)):
		print('{} - {} - {} Credits'.format(results[idx], classified_results[idx], credits[idx]))




