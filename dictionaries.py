#A Simple Dictionary

#alien_0 = {'color': 'green', 'points': 5}

#print(alien_0['color'])
#print(alien_0['points'])

#Working With Dictionaries

#simply a set of key-value pairs in {}'s attached together by a :
#the first item being the key and the second being the value; providing the key will give you the value
#these key pairs are seperated by a ','
#you access this value by providing the dictionary name next to the [key]

#Adding New Key-Value Pairs

#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)
#adding to the dict works the same way with empty {}

#Modifying Values in a Dictinary

#alien_0['color'] = 'orange'
#print(alien_0['color'])

#alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
#if alien_1['speed'] == 'slow':
    #x_increment = 1 
#elif alien_1['speed'] == 'medium':
    #x_increment = 2
#else:
    #x_increment = 3

#alien_1['x_position'] = alien_1['x_position'] + x_increment
#print(f"New position: {alien_1['x_position']}")

#Removing Key-Value Pairs

#computer = {'material':'metal','energy':'electricity', 'users':'humans'}
#del computer['users']
#print(computer)

#Dictionary of Similar Objects

#fav_languages = {
    #'osiah':'rust',
    #'turing':'python',
    #'vitalik':'serpent',
    #'descartes':'solidity',
    #}
#basic syntax: use return in the middle of {}, define your dict, end it by lining the ending brace up with the dict

#language = fav_languages['osiah'].title()
#print(f"Osiah's favorite language is {language}.")

#Using get() to Access Values

#computer = {'material':'metal','energy':'electricity', 'users':'humans'}
#consciousness = computer.get('mind', 'no consciousness assigned')
#if the key named 'mind' is in the dict it'll print the value, if not we get a clean message instead of an error
#print(consciousness)

#TRYITYOURSELF
#Person
#hilbert = {'craft': 'mathematicain', 'age':'old', 'way_of_mind':'logical'}
#print(hilbert['age'])
#print(hilbert['craft'])
#print(hilbert['way_of_mind'])

#Favorite Numbers

#fav_numbers = {
    #'john':'3',
    #'paul':'7',
    #'kobe':'24',
    #'turing':'69',
    #'einstein':'0',
#}
#for key, value in fav_numbers.items():
    #print(f"{key.capitalize()}'s favorite number is {value}.")

#Glossary

#programming_words = {'for':'loop','del':'delete','print':'say','def':'function', '**':'squared'}
#for key, value in programming_words.items():
    #print(f"{key}, {value}\n")

#Looping Through All Key-Value Pairs

#user_0 = {
    #'username':'tbag',
    #'first': 'alan',
    #'last':'turing',
    #}
#for k, v in user_0.items(): #the variables for the key and value can be anything; only rule is the , seperation
    #items() simply returns a sequence of key value pairs
    #the for loop then assigns each of the pairs to the 2 variables provided
    #print(f"\nKey: {k}")
    #print(f"Value: {v}")
    
#fav_languages = {
    #'osiah':'rust',
    #'turing':'python',
    #'vitalik':'python',
    #'newton':'solidity',
    #}
#for name, language in fav_languages.items():
    #print(f"{name.title()}'s favorite language is {language.title()}.\n")

#Looping Through All Keys in a Dictionary

#for name in fav_languages.keys():
    #print(f"{name.title()} voted today.")

#for name in fav_languages: #looping through the keys is the defualt behaviour when looping through a dict
    #print(name.title())#produces the same result as the code above

#friends = ['newton', 'vitalik']
#for name in fav_languages:
    #print(f"What's up {name.title()}.")

    #if name in friends:
        #language = fav_languages[name].title()
        #print(f"\t{name.title()}, I  see you're enjoying {language}.")
    #if 'eric' not in fav_languages:
        #print(f"Eric, please take your poll!")

#Looping Through a Dictionaries Keys in Order

#for name in sorted(fav_languages):
    #print(f"{name.title()}, thank you for taking the poll!")

#Looping Through All Values in a Dictionary
#for langs in fav_languages.values():
    #print(f"{langs.title()} is a great language!")

#SETS

#print(set(fav_languages.values()))
#set() simply takes any repeating items out and creates a unique set

#this_is_a_set = {'gpu', 'cpu', 'ssd', 'ram', 'ram'}
#print(this_is_a_set)
#don't mistake a dict for a set; sets are built with {}'s but have no key-value pairs

#TRYITYOURSELF
#Glossary 2

#programming_terms = {
    #'for':'loop',
    #'del':'delete',
    #'print':'say',
    #'def':'function',
    #'**':'squared',
    #'*':'multiply',
    #'if':'conditional test',
    #'""':'string',
    #'tuple':'immutable list'
    #}

#for key, value in programming_terms.items():
    #print(f"{key}, {value}\n")

#Rivers

#rivers = {
    #'Mississippi River':'NA',
    #'Volga River':'EU',
    #'Zambezi River':'Africa'
    #}

#for river_name, country in rivers.items():
    #print(f"The {river_name} is in {country}.")
    #if river_name in rivers:
        #print(f"\n{river_name}")
    #if country in rivers.values():
        #print(f"{country}\n")

#.items() is extremely important because it lets the program know that the items you listed are key-value pairs
#without .items it returns an error saying that there's too many items to unpack
#meaning the number of variables doesn't match the number of values; i.e. river_name, country in rivers
#so to let python know that they're connected key-value pairs you must use .items()

#Polling

#fav_languages = {
    #'osiah':'rust',
    #'turing':'python',
    #'vitalik':'serpent',
    #'newton':'solidity',
    #}

#should_take_poll = ['turing', 'mauchly', 'jennings', 'newton', 'vitalik']

#for name in should_take_poll:
    #if name in fav_languages:
        #print(f"Thanks {name.title()}, for responding!\n")
    #else:
        #print(f"{name.title()}, would you like to take my survey?\n")

#NESTING

#A List of Dictionaries

#alien_0 = {'color':'green','points': 5}
#alien_1 = {'color':'orange','points': 7}
#alien_2 = {'color':'blue','points': 10}

#aliens = [alien_0, alien_1, alien_2]
#for alien in aliens:
    #print(alien)

#aliens = []

#for alien_number in range(25):
    #new_alien = {'color':'green', 'points': 5, 'speed':'slow'}
    #aliens.append(new_alien)

#for alien in aliens[:3]:
    #if alien['color'] == 'green':
        #alien['color'] = 'yellow'
        #alien['speed'] = 'medium'
        #alien['points'] = 10

#for alien in aliens[:5]:
    #print(alien)

#A List Inside a Dictionary

#pizza = {
    #'crust':'thick',
    #'toppings':['mushrooms', 'chicken'] #basically you can turn the value from the pair into a list
    #}

#print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
#for topping in pizza['toppings']:
    #print(f"\t{topping}")

#fav_languages = {
    #'osiah':['rust','vyper','python'],
    #'turing':['python', 'pearl', 'fortran'],
    #'vitalik':['vyper','serpant', 'python'],
    #'newton':['solidity', 'javascript'],
    #}

#for name, languages in fav_languages.items():
    #print(f"\n{name.title()}'s favorite languages are:")
    #for language in languages:
        #print(f"\t{language.title()}")

#A Dictionary in a Dictionary

#users = { #this one looks complex but it's not; the VALUES ARE DICTIONARIES!
#'aeinstein':{#key 1
    #'first': 'albert',
    #'last': 'einstein',
    #'location': 'princeton'
    #},

#'mcurie': {#key 2
    #'first': 'marie',
    #'last': 'curie',
    #'location': 'paris',
    #},

#}

#for username, user_info in users.items():
    #each key is assigned to the variable username(2 keys total)
    #the variable user_info has 3 keys:'first', 'last' and 'location'
    #user_info is a variable that equals a value in a dictionary that holds another dictionary; therefore allowing it to hold 3 keys
    #print(f"\nUsername:{username}")
    #full_name = f"{user_info['first']} {user_info['last']}"
    #location = user_info['location']

    #print(f"\tFull name:{full_name.title()}")
    #print(f"\tLocation:{location.title()}")

#TRYITYOURSELF

#People

#albert = {
    #'craft': 'physics',
    #'first':'albert',
    #'last':'einstein',
    #}

#alan = {
    #'craft':'mathematics',
    #'first':'alan',
    #'last':'turing',
    #}

#vitalik = {
    #'craft': 'computer science',
    #'first': 'vitalik',
    #'last': 'buterin',
    #}

#people = [albert, alan, vitalik]

#for person in people:
    #print(person)

#Pets

#animal_0 = {'kind':'cat', 'owner_name':'john', 'age': 5}
#animal_1 = {'kind': 'elephant', 'owner_name': 'billy', 'age': 12}
#animal_2 = {'kind': 'snow leopard', 'owner_name': 'nature', 'age': 20}

#pets = [animal_0, animal_1, animal_2]

#for animal in pets:
    #print(animal)

#Favorite Places

#fav_places = {
    #'hilbert': 'math room',
    #'alan': 'computer room',
    #'wozniak': 'tinkering garage',
    #}

#for person, place in fav_places.items():
    #print(f"\n{person.title()}, {place}")

#Favorite Numbers

#fav_numbers = {
    #'john':['3', '5', '9'],
    #'paul':['7', '22'],
    #'kobe':['24', '11'],
    #'turing':['69', '5'],
    #'einstein':['0', '17'],
    #}

#for name, numbers in fav_numbers.items():
    #print(f"\n{name.title()}'s favorite numbers are:" )
    #for number in numbers: #looks like since there's multiple values in the key we have to create another variable that pulls each value out of 'numbers'
        #print(f"\t{number}")

#Cities

#cities = {
    #'newport news': {
        #'country': 'north america',
        #'population': 184600,
        #'fact':'named after Christopher Newport'},

    #'austin': {
        #'country': 'north america',
        #'population': 964177,
        #'fact':'wasn\'t always the capitol of Texas'},
    
    #'dallas':{
        #'country': 'north america',
        #'population': 1200000,
        #'fact': 'largest landlocked metropolitan area'},
        #}
    
#for city, city_info in cities.items():
    #country = f"Country:{city_info['country']}"
    #population = f"Population: {city_info['population']}"
    #fact = f"Fact: {city_info['fact']}"
    #print(f"\tCity: {city.title()}")
    #print(f"\n{country.title()}\n{population}\n{fact}\n")

#Extensions

program_crafting = {
    'osiah':{
        'language':'rust',
        'project':'EVM Venturer'},

    'turing':{
        'language': 'vyper',
        'project':'AGI Contract'},

    'vitalik':{
        'language': 'python',
        'project':'Ethereum'},

    'newton':{
        'language': 'c++',
        'project':'Alchemy'},
    }
for name, program_info in program_crafting.items():
    print(f"\t{name.title()}:\n")
    language = f"Language: {program_info['language']}"
    project = f"Project: {program_info['project']}"
    print(f"{language.title()}\n{project}\n")
