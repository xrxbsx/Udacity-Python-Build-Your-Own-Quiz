from string import Template


def checkAnswer(answer, questionNumber):
	'''
			answer: string --> answer that user typed
	questionNumber: number --> the current question number 
	'''
	if questionNumber == 1 and answer.lower() == 'function':
		return True
	elif questionNumber == 2 and (answer.lower() == 'parameters' or answer.lower() == 'arguments'):
		return True
	elif questionNumber == 3 and answer == 'None':
		return True
	elif questionNumber == 4 and answer == 'list':
		return True
	else:
		return False

# construct the template string for our quiz
fulltextTemplate = Template('''
	A $blank1 is created with the def keyword. You specify the inputs a function 
	takes by adding $blank2 separated by commas between the parentheses. ${blank1}s by default
	returns $blank3 if you don't specify the value to return. $blank2 can be standard data types such as
	string, number, dictionary, tuple, and $blank4 or can be more complicated such as objects and
	lambda functions.
''')

# construct the substitution dictionary for our template string
substitution = {
	'blank1': '__1__',
	'blank2': '__2__',
	'blank3': '__3__',
	'blank4': '__4__'
}


current = 1;
total = 4
while current <=total:
	string = fulltextTemplate.substitute(substitution);
	question = 'What should go in blank number ' + str(current) + '?'
	print(string)
	print(question)
	readAnswer = input()
	if checkAnswer(readAnswer, current):
		# right answer
		substitution['blank'+str(current)] = readAnswer
		print('Right Answer!')
		current += 1
	else:
		# wrong answer
		print('Wrong Answer!')
	print('\n--------------------------------------------------------------------------------\n')

print('Congradulation! You have passed the quiz!')

