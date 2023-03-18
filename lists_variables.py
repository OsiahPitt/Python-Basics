#USING VARIABLES IN STRINGS
#first_name = "ada"
#last_name = "lovelace"
#full_name = f"{first_name} {last_name}"
#print(full_name)

#first_name = "ada"
#last_name = "lovelace"
#full_name = f"{first_name} {last_name}"
#print(f"Hello, {full_name.title()}!")

#first_name = 'Osiah'
#last_name = 'Pitt'
#full_name = f"{first_name} {last_name}"
#message = f"Hello, {first_name} {last_name.title()}!"
#print(message)

#ADDING WHITE SPACE(\t and \n)
#print("\tPython")
#print('Python')

#print('Language: \nPython\nC+\nJava\nPascal')

#print('Languages:\n\tPython\n\tJava\n\tPascal\n\tRuby')

#STRIPPING WHITESPSACE
#favorite_language = 'Python '
#favorite_language.rstrip() #same thing with .lstrip()

#faorite_language = ' Python '
#favorite_language.strip() 

#REMOVE PREFIXES .removeprefix('')
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
'nostarch.com'

#WORKING WITH PART OF A LIST

#Slicing A List
players = ['12', '23', '24', '30', '11', '19']
#print(players[0:3])
#print(players[:3])#omitting the first index makes python automatically run it from the beginning
#print(players[2:])#same thing if you omit the second index
#print(players[-3:])# negative integers takes the last items from a list
#print(players[0:1:2])#works similar to range with being able to take 3 arguments but not sure how exactly
#so the way the 3 argument slice works is: [start:stop:steps]; i.e. >>> list[::2] (simply prints the list from start to stop in 2 step)
print(players[:4:2]) #meaning print index 0-4 in 2 step
#Looping Through A Slice
#for player in players[:2]:
    #print(f'{player} is one of our best guys.')
    
    
    
 

#ORGANIZING A LIST

#sorting a list permanently using .sort() method
cars = ['bmw', 'audi', 'toyota', 'subaru',]
#cars.sort()
#.sort() permanently changes the order to alphabetical
#(reverse=True) simply executes the reverse of .sort()
#cars.sort(reverse=True)


#print(sorted(cars)) #sorted function isn't permanent and allows you to return back to the og list, also doesn't require .sorted but is used inside of the print function
#sorted() can also accept a reverse=True argument as well
#print(cars)

#PRINTING LIST IN REVERSE ORDER using .reverse() function
#cars.reverse()
print(cars)
#this function is permanent like .sort but can be reverted back to the og list by using .reverese() again

#there's some interesting relationship between methods that are used like list.(reverse) or .sort, 

#FINDING THE LENGTH OF A LIST using len() function
len(cars)

#Copying A List
my_foods = ['sweet potato', 'venison', 'bananas']
friends_foods = my_foods[:] #simply copies the original list; creates a seperate identical list, using append() on one won't perform it on the other
print(friends_foods)

#MODIFYING ELEMENTS IN A LIST
motorcycles = ['honda', 'suzuki', 'yamaha']
#motorcycles[0]= 'ducati'
#print(motorcycles)

#ADDING ELEMENTS TO A LIST
#(appending elements to the end of a list; .append())

#motorcycles.append('ducati') #doesn't require an equals like the mod above does^
#print(motorcycles)

#motorpickles = [] #(.append() allows for easily building dynamic lists)
#motorpickles.append('dill')
#motorpickles.append('kosher')
#motorpickles.append('ducati')

#print(motorpickles)

#INSERTING ELEMENTS INTO A LIST(.insert())
#motorcycles.insert(2, 'ducati') #simply specify the index and then add the value that needs to be placed there
#print(motorcycles)

#REMOVING ELEMENTS FROM A LIST(del statement)
#del motorcycles[2] #just the statement followed by the list and index that needs deletion
#print(motorcycles)

#REMOVING AN ITEM USING .pop()
#the pop method simply removes the last item from the list; like popping something off of a stack, the top of the stack being the end of the list 
#the other difference between pop method and del statement is that the popped off item can still be used; del is a permanent deletion
#popped_motorcycles = motorcycles.pop() #interesting note: initially used pop method alone on motorcycles and, it worked as planned but then assigned it to a variable and it kept it popped off and the second printing ended with the final item
#print(popped_motorcycles)

#.pop() not only pops it off but uses only what was popped off

#print(motorcycles)
#popped_motorcycles = motorcycles.pop()
#print(popped_motorcycles)

#last_owned = motorcycles.pop()
#print(f"The last time I rode a {last_owned.title()} I got hit by a pigeon.")

#POPPING ITEMS FROM ANY POSITION IN THE LIST
#first_owned = motorcycles.pop(1)
#print(f"We had a lot of fun on the {first_owned.title()} and may buy our own.")

#use del for perma deleting and pop if you want to use that deleted item

#REMOVING AN ITEM BY VALUE
#the .remove() method is for when the position of the item is unkown but you know the value of that item
motorcycles.remove('yamaha')
print(motorcycles)

#can also be used to manipulate the item being removed 
too_fast = 'suzuki'
motorcycles.remove(too_fast)
print(f'\n{too_fast.title()} is a great brand but their bikes are too dangerous.')

#LISTS
#it's a good idea to make the names of lists plural i.e letters, digits, etc.
#[] indicate lists 

bicycles = ['trek', 'cannondale', 'specialized', 'redline']
#print(bicycles)

#ACCESSING ELEMENTS IN A LIST
#print(bicycles[0]) #[0[] being the first position of the index, 1 being the second, etc.
#print(bicycles[-1]) #[-1] always refers to the last item in the list, [-2] returning the 2nd from last, etc.

#You can use individual values from a list as you would any other variable

message = (f'He went out and a bought a brand new {bicycles[1].title()} and broke it immediately!')
print(message)




#MAKING NUMERICAL LISTS using the range() function
#for value in range(1, 5):
    #print(value)
    #the range() function makes python start counting at the first value you give it and stop before the second

#for values in range(1, 6):
    #print(values)

#for value in range(11):
    #print(value)

#numbers = list(range(11))
#print(numbers)
#by wrapping the list function around the range function you can create a list of numbers in that specfic range

#even_numbers = list(range(2, 11, 2)) #passing the function 3 arguments here adds 2+2 until it hits or goes past 11
#print(even_numbers)

#squares = []
#for value in range(1,11):
    #square = value ** 2
    #squares.append(square)
#print(squares)
#creates a variable called 'sqaures' that represents an empty list, then the using the for loop we create another variable
#called 'value' wich represents a range of numbers from 1-10, yet another variable is created called 
#'square' which takes that range of numbers from above and and raises it to the 2nd power **
#next that initial empty list called 'squares' uses the .append() function to add pull all of those squares into 
#that beautiful empty list; thus printing a list of the squares of 1-10

#squares = []
#for value in range(1,11):
    #squares.append(value ** 2)
#print(squares) #even simpler version of the program

#SIMPLE STATISTICS WITH A LIST OF NUMBERS
#min, max, sum functions
#digits = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 0]
#print(min(digits))
#print(max(digits))
#print(sum(digits))

#LIST COMPREHENSIONS
#combines the for loop and new elements into one line while simultaneously appending each element
#notnice how there's no ; at the end of the for statement
#from 4 lines of code, to 3 and then 1; all accomplissh the same task but this one is much more efficient
#squares = [value ** 2 for value in range(1,11)]
#print(squares)

squared_odds = [numbers ** 2 for numbers in range(1,16,2)]
print(squared_odds)






#LOOPING THROUGH AN ENTIRE LIST
magicians = ['babbage', 'houdini', 'lovelace']
for magician in magicians: 
    #print(magician)
    #defines a for loop by pulling a name from the list(magicians) and associating it with a variable(magician)
    #by printing the variable created in the for loop we're saying "For every magician in the list of magicians, print the magician's name."
    #the variable can be names anything you want
    #everything that's indented is considered "inside" the loop
    # print(f'{magician.title()}, that was a good trick!')
    print(f'I can\'t wait to see your next one, {magician.title()}.\n')
    print(f'Thank you, everyone. That was a great performance!')
    #notice how line 11 isn't indented and only is printed once

#COMMON INDENTATION ERRORS
#1.Forgetting to indent the line after the for statement in a loop






#NAMES
names = ['Sally', 'Bobby', 'Ricky', 'Dylan', 'Morat']
#print(name[0])
#print(name[1])
#print(name[2])
#print(name[3])
#print(name[4])

#GREETINGS
print(f"Hey {names[0]}, how have you been?")
print(f"Hey {names[1]}, how have you been?")
print(f"Hey {names[2]}, how have you been?")
print(f"Hey {names[3]}, how have you been?")
print(f"Hey {names[4]}, how have you been?")

#YOUR OWN LIST
#transportations = ['car', 'plane', 'mouse', 'train' ] 
#print(f'I would like to ride in a {transportations[0]}')
#print(f'Who wants to fly on the {transportations[1]}?')
#print(f'How much cash would it cost me to fly on that {transportations[2]}?')
#print(f'What time is the {transportations[3]} coming?')






#GUEST LIST
dinner_list = ['Einstein', 'Hilbert', 'Turing']
#print(f"Hey {dinner_list[0]}, would you be able to make it to a small dinner on Saturday?")
#print(f"Hey {dinner_list[1]}, would you be able to make it to a small dinner on Saturday?")
#print(f"Hey {dinner_list[2]}, would you be able to make it to a small dinner on Saturday?")

#CHANGING GUEST LIST
not_coming = 'Hilbert'
dinner_list.remove(not_coming)
dinner_list.insert(1, 'Tao')
#print(f'Hey {dinner_list[0]}, {not_coming} can\'t make it but {dinner_list[1]} is able to come and fill his spot.')
#print(f'Hey {dinner_list[2]}, {not_coming} can\'t make it but {dinner_list[1]} is able to come and fill his spot.')
#print(f'Hey {dinner_list[1]}, thanks for saving the show and filling {not_coming}\'s spot!')

#MORE GUESTS
dinner_list.insert(0, 'Descartes')
dinner_list.insert(2, 'Galileo')
dinner_list.append('Plato')
#print(dinner_list)

#print(f"Hey {dinner_list[0]}, found a bigger table so it would be my honor if you could make it to dinner.")
#print(f"Hey {dinner_list[1]}, found a bigger table so there'll be three more guests that I think you'll enjoy.")
#print(f"Hey {dinner_list[2]}, found a bigger table so would dinner still be of interest to you?")
#print(f"Hey {dinner_list[3]}, found a bigger table so there'll be three more guests who you'll love.")
#print(f"Hey {dinner_list[4]}, found a bigger table so there'll be three more guests to liven up the event.")
#print(f"Hey {dinner_list[5]}, found a bigger table so there's a spot with your name on it if you're interested.")

popped_guest0 = dinner_list.pop(5)
popped_guest1 = dinner_list.pop(4)
popped_guest2 = dinner_list.pop(3)
popped_guest3 = dinner_list.pop(2)


#print(f"\nNow there can only be two guests because the table was stolen through osmosis.")
#print(f'Sorry to cancel like this {popped_guest0} but the table was stolen.')
#print(f'Sorry to cancel like this {popped_guest1} but the table was stolen.')
#print(f'Sorry to cancel like this {popped_guest2} but the table was stolen.')
#print(f'Sorry to cancel like this {popped_guest3} but the table was stolen.')

#print(dinner_list)

#print(f'\nHey {dinner_list[0]} the table was stolen but you and {dinner_list[1]} are still invited.')
#print(f'\nHey {dinner_list[1]} the table was stolen but you and {dinner_list[0]} are still invited.')

#del dinner_list[0]
#del dinner_list[1]

dinner_list = dinner_list.insert(0, 'Will')

print(dinner_list)

#MOST IMPORTANT THINGS LEARNED FROM THIS EXERCISE:
#1.That .remove, .insert, .append, and del all don't need to = a variable and can be used on their own 







#SEEING THE WORLD
#visits = ['Berlin', 'Spain', 'Brazil', 'Ireland', 'Boston']
#print(sorted(visits))
#print(visits)

#visits.reverse() #can't just put .reverse; needs to be .reverse()
#visits.reverse()
#visits.sort(reverse=True)
#print(visits)

#DINNER GUESTS
#dinner_list = ['Einstein', 'Hilbert', 'Turing']
#print(f'Glad all {len(dinner_list)} of the homies could make it tonight!')

#EVERY FUNCTION
languages = ['English', 'Russian', 'Thai', 'Japanese']
languages[2] = 'French'
languages.append('Thai')
languages.insert(0, 'German')
del languages[0]
holding_off = languages.pop()
already_know = 'English'
languages.remove(already_know)
#in the 21st line it shows that we're able to make a variable equal a list using .pop() 
#in lines 22 and 23 we must make a variable which equals an already existing item and then perform .remove on it 

print(f'I\'d like to learn {languages[0]} this year. In the next few years it also seems smart to learn {languages[1]} but we\'ll see. Another one that would come in handy is {languages[2]}. Good thing I already know {already_know}. At least for the next decade though I won\'t be learning \n{holding_off}. That\'s about {len(languages)} for the near future which is a good amount.')


#print(languages)
languages.reverse()
#print(languages)
print(len(languages))
print(languages[2])
