#!/usr/bin/python

#! : Shebang
# /usr/bin/python : Absolute path to the python software

" Comments in Python :"
#	1. Single Line  : #, '', "", ''' ''' & """ """
#	2. Multi Line   : ''' ''' & """ """

''' 
Rule of Creating Variables in Python
	1. A-Z
	2. a-z
	3. 0-9
	4. _
	5. A-Za-z
	6. A-Za-z0-9
	7. A-Za-z0-9_
Note: Do not use numeric values as prefix to variable name
Ex : 007 = "Welcome to Python World"
'''
'Creating Variables in Python'

# String Variables must be created under quotes '' , " ", ''' ''' & """ """

FirstName = 'Guido'
middleName = "Van"
_Last_Name = '''Rossum'''
_Duration  = 60
SoftwareVersion = 3.6
_007 = "Welcome to Python World"

"Accessing Variables in Python :"

print(FirstName)
print('')
print(middleName)
print('')
print(_Last_Name)
print("")
print(_Duration)
print("")
print(SoftwareVersion)
print("")
print(_007)
