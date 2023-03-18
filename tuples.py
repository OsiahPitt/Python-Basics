#DEFINING A TUPLE

#Tuples are simply lists that cannot be changed(immutable); (regular lists can be changes, therefore being mutable)
#They look just like lists but use ()'s instead of []'s 

#dimensions = (200, 50)
#print(dimensions[0])
#print(dimensions[1])

#dimensions[0] = 250 #gives an error because values in tuples cannot be changed
#Tuples are defined by the presence of a comma; if you want to define a tuple with 1 element you need to add comma i.e. (11,)

#WRITING OVER A TUPLE
#print("Original dimensions:")
#for dimension in dimensions:
    #Print(dimension)

#this reassigns the variable instead of changing the tuple which python considers valid
#dimensions = (400,100)
#for dimension in dimensions:
    #print(dimension)

#TRYITYOURSLEF-7
#Buffet:
basic_foods = ('apple', 'pear', 'cucumber', 'spinach', 'wild rice')
for foods in basic_foods:
    print(foods)

#basic_foods[0] = 'pineapple'

basic_foods = ('\nmango', 'avocado', 'cucumber', 'spinach', 'wild rice')
for foods in basic_foods:
    print(foods)
