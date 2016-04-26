### written in python3
### by CreatCodeBuild@github.com
### 2016/04/25

from string import Template


# construct the template string of each level for our quiz
# level 1, easy
level1 = '''
	A $blank1 is created with the def keyword. You specify the inputs a function 
	takes by adding $blank2 separated by commas between the parentheses. ${blank1}s by default
	returns $blank3 if you don't specify the value to return. $blank2 can be standard data types such as
	string, number, dictionary, tuple, and $blank4 or can be more complicated such as objects and
	lambda functions.
'''

# level 2, medium
level2 = '''
	The $blank1 statement in Python differs a bit from what you may be used to in C or Pascal. 
	Rather than always iterating over an arithmetic progression of numbers (like in Pascal), or 
	giving the user the ability to define both the iteration step and halting condition (as C), 
	Python’s $blank1 statement iterates over the items of any sequence (a list or a string), in the 
	order that they appear in the sequence.

	The $blank2 statement, like in C, breaks out of the smallest enclosing for or while loop.

	Loop statements may have an $blank3 clause; it is executed when the loop terminates through 
	exhaustion of the list (with for) or when the condition becomes false (with while), but not 
	when the loop is terminated by a $blank2 statement.

	When used with a loop, the $blank3 clause has more in common with the $blank3 clause of a try 
	statement than it does that of if statements: a try statement’s $blank3 clause runs when no 
	exception occurs, and a loop’s $blank3 clause runs when no $blank2 occurs.

	The $blank4 statement, also borrowed from C, ${blank4}s with the next iteration of the loop.

	The $blank5 statement does nothing. It can be used when a statement is required syntactically 
	but the program requires no action.
'''

# level 3, hard
level3 = '''
	A $blank1 definition is an executable statement. Its execution binds the $blank1 name in the 
	current local namespace to a $blank1 object (a wrapper around the executable code for the $blank1). 
	This $blank1 object contains a reference to the current global namespace as the global namespace to 
	be used when the $blank1 is $blank2.

	The $blank1 definition does not execute the $blank1 body; this gets executed only when the $blank1 is $blank2.

	Small anonymous ${blank1}s can be created with the $blank3 keyword. $blank3 functions can be used 
	wherever function objects are required. They are syntactically restricted to a $blank4 expression. 
	Semantically, they are just syntactic sugar for a normal $blank1 definition. Like nested $blank1 
	definitions, $blank3 functions can reference variables from the containing scope.
'''

# construct the substitution dictionary for our template string
substitution = {
	'blank1': '__1__',
	'blank2': '__2__',
	'blank3': '__3__',
	'blank4': '__4__',
	'blank5': '__5__'
}

# solution of level 1
solution1 = {
	'blank1': 'function',
	'blank2': 'parameters',
	'blank3': 'None',
	'blank4': 'list'
}

# solution of level 2
solution2 = {
	'blank1': 'for',
	'blank2': 'break',
	'blank3': 'else',
	'blank4': 'continue',
	'blank5': 'pass'
}

# solution of level 3
solution3 = {
	'blank1': 'function',
	'blank2': 'called',
	'blank3': 'lambda',
	'blank4': 'single'
}


def check_answer(answer, question, solution):
	'''
	  answer: string --> answer that user typed
	question: string --> the current question key in solution
	solution: string --> the solution dictionary 
	return True if answer is the solution of the question
		  False if answer is not the solution
	'''
	#  first check if the [question] key is a valid key
	#  if valid, get the value of this key and compare it with the solution
	if solution.get(question) != None and solution[question] == answer:
		return True
	else:
		return False


def get_level():
	'''
	ask the user which level to play,
	get the corresponding level template and solution,
	return a tuple (level, solution)
	   level: Template --> the corresponding string template of the user selected level
	solution: dict     --> the solution dictionary of the corresponding level
	'''
	print('Please choose a difficulty level from easy / medium / hard')
	levelTemplate = None		#  refers to the string template, initialized as None
	solution = None				#  refers to the dict solution,   initialized as None
	while(solution == None):	#  when there is no solution, keep asking user to select a valid level
		level = input()
		if(level == 'easy'):
			#  easy --> level 1
			levelTemplate = Template(level1)
			solution = solution1
		elif(level == 'medium'):
			#  medium --> level 2
			levelTemplate = Template(level2)
			solution = solution2
		elif(level == 'hard'):
			#  hard --> level 3
			levelTemplate = Template(level3)
			solution = solution3
		else:
			#  user didn't type any valid level
			print('Please choose a real level that actually exists!')
	print('You choosed level ' + level)
	return (levelTemplate, solution)


def main():
	levelTemplate, solution = get_level()	#  the string template of the selected level
	current = 1				#  current question number
	total = len(solution)	#  the total question numbers, is the size of solution

	while current <= total:
		string = levelTemplate.substitute(substitution);
		question = 'What should go in blank number ' + str(current) + '?'
		print(string)
		print(question)
		readAnswer = input()
		blank = 'blank'+str(current)	#  get the key corresponding to the current question
		if check_answer(readAnswer, blank, solution):
			# right answer
			substitution[blank] = readAnswer	#  modify the template, replace blanks __x__ with answers
			print('Right Answer!')
			current += 1
		else:
			# wrong answer
			print('Wrong Answer!')
		print('\n--------------------------------------------------------------------------------\n')

	print(levelTemplate.substitute(substitution))
	print('Congradulation! You have passed the quiz!')


main()
