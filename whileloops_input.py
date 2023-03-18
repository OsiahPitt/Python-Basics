#How the input() Function Works

#message = input("Tell me something and I'll repeat it back to you: ")
#print(message)

#Writing Clear Prompts

#name = input("Please enter your name: ")
#print(f"\nHello, {name}!") 

#prompt = "If you share your name we can personalize the messages you see."
#prompt += "\nWhat is your first name? " # += operator takes the original string and adds the new string on to the end

#name = input(prompt)
#print(f"\nHello, {name}!")

#Using int() to Accept Numerical Input

#age = input("How old are you? ")
#age = int(age)

#if age >= 18:
    #print(True)

#height = input("How tall are you, in inches? ")

#height = int(height)

#if height >= 48:
    #print("\nYou're tall enough to ride!")
#else:
    #print("\nMaybe next time dude.")

#Introducing While Loops

#current_number = 1 
#while current_number <= 5:
    #print(current_number)
    #current_number += 1 # += operator also allows you to add numbers 

#Letting the User Choose When to Quit

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "

#message = ''
#while message != 'quit':
    #message = input(prompt)
    #if message != 'quit':
        #print(message)

#Using a Flag

#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "

#active = True #a flag essentially gives the while loop freedom to have many conditionals available 
#while active:
    #message = input(prompt)
    #if message == 'quit':
        #active = False
    #else:
        #print(message)
    
#Using the break statement to Exit a Loop

#prompt = "\nTell me some of the cities you've visited:"
#prompt += "\n(Enter 'quit' when you are finished.) "

#while True: #while True will run forever unless it hits a break statement
    #city = input(prompt)

    #if city == 'quit':
        #break
    #else:
        #print(f"I'd love to go to {city.title()}!")

#Using continue in a loop

#current_number = 0
#while current_number < 10:
    #current_number += 1
    #if current_number % 2 == 0: #leaves out all even numbers because 2 % any even number is 0; no remainder
        #continue
    #print(current_number)

#Avoiding Infinite Loops

#x = 1 #ctrl-c to stop the loop
#while x <= 5:
    #print(x)

#TRYITYOURSELF

#PC PARTS

#prompt = ("\nWhat part do you need replaced in your computer?")
#prompt += ("\nEnter 'quit' to stop adding parts. ")

#message = ''
#while message != 'quit':
    #message = input(prompt)

    #if message != 'quit':
        #print(f"\nReplacing {message} now!")

#Movie Tickets

#age = input("How old are you?")
#age = int(age)

##while age < 3:
    #print('Your ticket is free.')
    #if age < 12:
        #print('Your ticket is $10')
    #else:
        #print("Your ticket is $15"
