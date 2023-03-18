#INTEGERS
# double asterisk (**) represents an exponent; raising to a power 
#python uses order of operations
#FLOATS are any number with a decimal point
#when writing long numbers its possible to use underscores to imorove readability (14_000_000_000)python ignores the _'s
#you can assign variables to more than one value i.e. x, y, z = 0, 0, 0

#a CONSTANT is a variable that remains the same throughout the life of the program; there's no built in constant types but Python programmers will use all caps instead i.e. MAX_ETHEREUM = 5000

#print(4*2)
#print(16/2)
#print(108-100)
#print(5+3)
#print(3**3)

#fav_number = 11
#message = f'My favorite number is {fav_number}!'
#print(message)

import this

#AVOIDING SYNTAX ERRORS
#message = "One of Python's strengths is its community."
#print(message)

#message = 'one of python's strengths is its community'
#print(message)
#python thinks the apostrophe is the end of the string; so you must use double quotes

#CHANGING CASE IN A STRING WITH METHODS(.title, .uppper, etc.)

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#PERSONAL MESSAGE

#name = 'Joshua'
#message = f"Hello {name}, would you like to learn some Javascript today?"
#print(message)
#print(f'Hello {name}, would you like to learn to read?')
#f-strings differ from normal strings in that they allow to replace parts of the string with a variable or some other data using f' and {}

#NAME CASES

#name = "John"
#print(name.lower())

#name = 'Zeke'
#print(name.upper())

#name = 'luther von neummann'
#print(name.title())

#QUOTE
#quote = '"Quality is not an act, it is a habit."'
#print(f'Aristotle once said, {quote}')
#philosopher = 'Aristotle'
#message = f'{philosopher} once said, {quote}'
#print(message)

#STRIPPING NAMES

#name = '  Ver\toni\nca '
#print(name.lstrip())
#print(name.rstrip())
#print(name.strip())

#FILE EXTENSIONS
filename = 'python_notes.txt'
refined = filename.removesuffix('.txt') #don't froget the quotes around what's being removed in the ('')
print(refined)

#Hello World

#message = "Hello Python World!"
#print(message)

#message = "Hello Python Crash Course World!"
#print(message)

#message = "Hello Python Crash Course Reader!"
#print(mesage)
