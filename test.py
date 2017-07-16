#this program says hello and asks for my name
print('hello world!')
print('what is your name?')
myName=input()
if myName == '':
	print('please enter your name')
else:
	print('your name is '+myName)
	print('the length of your name is:')
	print(len(myName))
	print('what is your age?')
	myAge=input()
	if myAge == '':
		print('please enter your age')
	else:
		print('you will be '+str(int(myAge)+1)+' in a year')
