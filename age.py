driving = input('do you drive before?')
if driving != 'yes' or driving != 'no':
	print('please reply yes or no'):
	raise SystemExit

age = input('how old are you?')
# need to casting 
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('passed')
	else:
		print('it is illegal')
elif driving == 'no':
	if age >= 18:
		print('you could get liscense')
	else:
		print('you gonna get liscense')