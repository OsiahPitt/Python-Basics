#Simple Example

#cars = ['bmw', 'audi', 'toyota', 'subaru']

#for car in cars:
    #if car == 'bmw':
        #print(car.upper())
    #else:
        #print(car.title())

#Conditional Tests

#every if statement has an expression that Python evaluates as True or False
#if true it gets printed, if not true it doesn't get printed

#Checking for Equality

#ozone = 'hacker'
#single = sign sets the value of ozone to hacker 
#ozone == 'hacker'
#double == checks if this is true or not (called an equality operator)

#Ignoring Case When Checking for Equality

#two values with with different capitalization aren't equal i.e. car = 'audi'car == 'Audi' would return false
#car = 'Audi' car.lower = 'audi' comes back as True

#Checking for Inequality using the inequality operator !=

#requested_topping = 'mushrooms'

#if requested_topping != 'anchovies':
    #print("Hold the anchovies!")

#Numerical Comparisons

#numbers work the exact same way

#number = 11

#if number != 12:
    #print('Wrong answer, try again.')

#other mathematical symbols such as <,>,<=, etc.

#age = 11
#if age != 12:
    #print('True')

#Checking Multiple Conditions

#the and/or operators help if you're checking multiple conditions at the same time

#age_0 = 22
#age_1 = 18

#if age_1 >= 21 and age_1 >= 21:
    #print('beacon')

#if age_1 <= 19 and age_0 >= 20 and age_0 < 23:
    #print('something')

#and allows you to check if multiple things are True or False at the same time; if one of these things are false then it renders the entire expression false and vice versa

#age1 = 25
#age2 = 19

#if age1 > 15 or age2 <= 12:
    #print('fuck yea bro')

#or acts in the same way but only needs one of the if conditionals to be true; only fails when both are false

#Checking Whether a Value Is In or Is Not In a List
#the in operator allows you to check if a value exists in a list 
#currencies = ['dollar', 'euro', 'pound', 'ruble', 'yuan']

#if 'dollar' in currencies and 'euro' in currencies:
    #print('yes')

#on the other hand, using is not in variable lets you see if something isn't in the list

#if 'monkey wrench' not in currencies:
    #print('Not here, sorry')

#BOOLEAN EXPRESSIONS
#a boolean is another form of conditional test which literally uses True and False do determine a conditions state
#game_on = True
#edit_builds = True

#TRYITYOURSELF-8
#Conditional Tests:

#car = 'bmw'
#if car != 'truck':
    #print('Cars are not trucks.')

#women = 'female'
#if women == 'female' and 'female' == women:
    #print(True)

#os_1 = 'apple'
#os_2 = 'microsoft'
#os_3 = 'linux'
#if os_1 == 'microsoft' or os_3 == 'linux':
    #print(True)

#prime = 7
#nonprime = 8
#if prime == 2+5 and nonprime == 2*4:

#interesting thing to note is that when printing True you don't need quotes
    #print(True)

#integer = 5
#rational_number = 1/2
#exponent = 3**3
#if (exponent < integer) or (rational_number != integer) and (exponent != integer):
#you can choose to add ()'s or not; helps with readability, simply seperate the expressions from the and, or operators with ()'s
    #print('math is the shit!')

#More Conditionals 
#prime = True
#nonporime = False
#if prime != False:
    #print(True)
 
#monkey = 'Chimp'
#if monkey.lower() == 'chimp':
    #print(True)

#integer_1 = 10
#integer_2 = 11
#integer_3 = 12
#if integer_1 <= integer_2 and integer_3 >= integer_2 and integer_2 != integer_3:
    #print(True)

#rock_1 = 'white'
#rock_2 = 'yellow'
#rock_3 = 'orange'

#if rock_3 and rock_2 != rock_2 and rock_3 and rock_1 or rock_2 and rock_3:
    #print('That\'s a lot of rocks sir.')

#sun = ['hot', 'bright', 'moving', 'energy', 'sphere']

#if 'hot' in sun or 'bimbo' in sun:
    #print('I love the sun.')

#if ('hot') or ('energy') not in sun: #don't understand why it's printing when both of them are in the list
    #print('Where\'s the sun?')

#if 'hot' or 'bright' not in sun: #literally makes no sense logically why it's printing; both items are in the list
    #print(True)

#IF STATEMENTS
#There are several different kinds of if statements and the choice of which to use depends on the # of conditions that need testing
#age = 20 #simplest if statement that exists, deals with a single conditional
#if age >= 18:
    #print('Somehow you\'re an adult now.')
    #print('Do you know at what age the brain has fully developed?')
    #indentation plays the same role here as it does in for loops; all indented lines get executed if the test passes

#IF-ELSE STATEMENTS
#the else statement allows you to perform a set of actions when the test fails

#age = 20
#if age < 18:
    #print('not old enough')
#else: print('welcome in')
#else statement works well in situations when you always want to execute one of two possible actions

#THE IF-ELIF-ELSE CHAIN
#elif is essentially another if test that runs only if the test before it fails; appropriate for when you just need one test to pass
#notice how you can put the : right after the else statement; if and elif require certain parameters and the colon goes after those paramaters, else simply has 1 built in paramater which is basically "if all else fails print me"

#age = 4

#if age < 4:
    #price = 0
#elif age < 18: 
    #price = 25
#else:
    #price = 40

#print(f"Your admission cost is ${price}.")
#also notice how you can place the same variable after each conditional with a different value and instead of writing over each other they execute according to the test; indentation mannn

#age = 65

#if age < 5:
    #price = 0
#elif age < 18:
    #price = 25
#elif age < 65.01:
    #price = 40
#else: #to be more precise you can simply omit the else statement and end it with elif; elif age <= 65:
        #price = 20

#print(f"Your admission cost is ${price}.")
#not sure why when age is 18 price is correctly $40 but when age is 65 price is $20 (adding a decimal works to fix it)

#TESTING MULTIPLE CONDITIONS
#os = ['apple', 'linux', 'microsoft']
#if 'apple' in os:
    #print("We definitely have a few apple systems in stock.")
#if 'linux' in os:
    #print("We definitely have a few linux systems in stocks.")
#if 'microsoft' in os:
    #print("We definitely have a few microsoft systems in stock.")
#print("Found the operating system you wanted to add to your new pc.")
#if the goal is for one block of code to run use elif, if you need multiple to run then simply use multiple if statements

#TRYITYOURSELF-9

#alien_color = 'green'
#if alien_color == 'green':
    #print('+5 Points')

#alien_color = 'blue'

#if alien_color == 'yellow':
    #points = '+5'
#elif alien_color == 'blue':
    #points = '+10'
#else: 
    #points = '+25'
#print(f'{points}') 

#age = 20
#if age < 2:
    #stage = 'baby'
#elif age < 4:
    #stage = 'toddler'''
#elif age < 13:
    #stage = 'kid'
#elif age < 20:
    #stage = 'teenager'
#elif age < 65:
    #stage = 'adult'
#else:
    #stage = 'elder'
#print(f"This person is in the {stage} stage of life.")


#fav_fruits = ['pear', 'avocado', 'banana']
#if 'pear' in fav_fruits:
    #print("I like pears!")
#if 'avocado' in fav_fruits:
    #print("I like avocados!")
#if 'banana' in fav_fruits:
    #print("I like bananas!")

#USING IF STATEMENTS WITH LISTS
#Checking For Special Items

#requested_toppings = ['green peppers', 'extra cheese', 'mushrooms', 'tomatoes', 'chicken', 'bacon']

#for requested_topping in requested_toppings:
    #if requested_topping == 'green peppers':
        #print(f"Sorry we're out of green peppers.")
    #else:
        #print(f'Adding {requested_topping}.') #do not forget about indentation; I just spent 2 hours on this baby program wondering why it wouldn't work, the else was out of the for loop and at first the if statement wasn't put fist so it wasn't executed

#print("\nYou're pizza is ready.")

#CHECKING THAT A LIST IS NOT EMPTY

#requested_part = []
#if requested_part: #using the name of a list in an if statement returns True if there's at least 1 item in the list; false if it's empty
    #for part in requested_part: #remember that 'if' is simply a conditional test and that 'for' is just creating a loop 
        #print(f"Adding {part}")
    #print("Finished building the pc!")
#else:
    #print('Are you sure you want a plain pc?') #the if statement returned false so it printed only the else statement

#USING MULTIPLE LISTS

#available_parts = ['gpu', 'cpu', 'ram','ssd',]
#requested_parts = ['gpu', 'hd', 'ram']

#for part in requested_parts:
    #if part in available_parts:
        #print(f'Adding {part.upper()}.')
    #if part not in available_parts:
        #print(f'Sorry, we\'re out of {part.upper()}s.')

#print("\nFinished with your new pc!")

#TRYITYOURSELF
#Hello Admin

#usernames = ['john', 'turing', 'ada', 'admin', 'harry']
#for names in usernames:
    #print(f'Welcome {names.capitalize()}, thank you for logging in!')
#else:
    #print("Hello admin, would you like to see a status report?")

#No Users

#usernames = []
#if usernames:
    #for names in usernames:
        #print(f'Welcome {names.capitalize()}, thank you for logging in!')
#if 'admin' in usernames:
    #print("Hello admin, would you like to see a status report?")
#else:
    #print("We need to get some new users!")

#Checking Usernames

#current_users = ['ada', 'einstein', 'turing', 'hilbert', 'jennings']
#new_users = ['peckert', 'steve', 'turing', 'wozniak', 'elizabeth']

#for name in new_users:
    #if name in current_users:
        #print(f"The name '{name.capitalize()}' is unavailable, please choose something else.")
    #else:
        #print(f"Congratulations {name.capitalize()}, you are now a registered user.")

#Ordinal Numbers

number_list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8, 9]

for numbers in number_list:
    if numbers == 1:
        print(f"{numbers}st")
    elif numbers == 2:
        print(f"{numbers}nd")
    elif numbers == 3:
        print(f"{numbers}rd")
    else:
        print(f"{numbers}th")
        
        
 


#meats = ['bison', 'venison', 'mahi-mahi', 'elk']
#for meat in meats:
    #print(meat)
    #print(f'{meat.title()} is very good for the body.\n')
#print(f'I feel strongly about the quality of nutritious meat!')

animals = ['lion', 'tiger', 'snow leopard']
for animal in animals:
    print(f'{animal.title()}\'s are better left in the wild.\n')
    print(f'What all {len(animals)} of these animals have in common is that they\'re vicious hunters.')
