Used_For="App Development"
Version=3.6

# Example 1:
# Note: Call or Access a variable using curly braces {}, are used as placeholders.

print(Used_For,id(Used_For),type(Used_For))
print("")
print(Version,id(Version),type(Version))
print("")
print('Python is used for {} and course is {}'.format(Used_For,Version)) 

# Example 2: 
# We can specify the order in which it is printed by using numbers (tuple index).
phone='Ipone7'
laptop="Mac Book Pro"
print('I like {0} and {1}'.format('Ipone7','Mac Book Pro'))
print('I like {1} and {0}'.format(phone,laptop))

# Example 3:
# We can use keyword arguments to format the string:

print('Hello {name}, {greeting}'.format(greeting='Goodmorning',name='John')) 
