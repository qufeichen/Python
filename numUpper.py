# program that accepts a sentence as console input and calculates the number of upper case letters and non-whitespace characters
#
# i.e. the input 'Hello    World!' will produce the following output:
# Upper 2
# Non-whitespace 11

def numUpper(str):
	upper = 0
	nonwhite = 0

	for x in range(0, len(str)):
		if str[x].isupper():
			upper += 1
		if str[x].isspace():
			nonwhite += 1

	print('Upper {0}'.format(upper))
	print('Non-whitespace {0}'.format(nonwhite))
	return;

# call function with user input from command line (python3 syntax)
str = input("input the text: ")
numUpper(str)
