#LIST COMPREHENSIONS
#combines the for loop and new elements into one line while simultaneously appending each element
#notnice how there's no ; at the end of the for statement
#from 4 lines of code, to 3 and then 1; all accomplissh the same task but this one is much more efficient
#squares = [value ** 2 for value in range(1,11)]
#print(squares)

squared_odds = [numbers ** 2 for numbers in range(1,16,2)]
print(squared_odds)



#COUNTING TO TWENTY
#count_twenty = [numbers for numbers in range(21)]
#print(count_twenty)

#ONE MILLION
#million = list(range(1,1000001))
#print(million)

#million = [numbers for numbers in range(1, 1000001)]
#print(million)

#SUMMING A MILLION
#million = list(range(1, 1000001))
#print(min(million))
#print(max(million))
#print(sum(million))

#ODD NUMBERS
#odds = [numbers for numbers in range(1, 20, 2)]
#print(odds)

#THREES
#multiplesofthree = [multiple * 3 for multiple in range(1, 11)]
#print(multiplesofthree)
#the 'multiple' represents the number that's is being multiplied by 3, starting at 1; so it goes 1*3, 2*3, etc.
#the for loop is what allows the numbers in the range to get multiplied one after the other

#CUBES
#cubes = [numbers**3 for numbers in range(1,11)]
#print(cubes)

#LIST COMPREHENSIONS ARE OP!





#SLICES
#digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#print(f'The first three items of the list are: {digits[0:3]}') #need to figure out how to remove the brackets
#print(f'Three items from the middle of the list are: {digits[3:6]} ')
#print(f'The last three items in the list are: {digits[7:]}')

#MY PIZZAS, YOUR PIZZAS
#meats = ['bison', 'venison', 'mahi-mahi', 'elk']
#friends_meats = meats[:]
# #3meats.append('salmon')
# friends_meats.append('lobster')

#my_fav = [og for og in meats[:]]
#print(f'My favorite meats are: {my_fav}')

#friends_fav = [og for og in friends_meats[:]]
#print(f'My friend\'s favorite meats are: {friends_fav}')

#print(f'My friends favorite meats are: {}')

#MORE LOOPS
myfoods = ['sweet potato', 'venison', 'bananas']
for foods in myfoods:
    print(foods)

meats = ['bison', 'venison', 'mahi-mahi', 'elk']
for meat in meats:
    print(meat)
