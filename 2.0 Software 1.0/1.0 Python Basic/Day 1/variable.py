# # # print('Hello DeepSeeds yo')
# # # name= 'JJ'

# # # print("Hello I am called " + name + ". Nice to meet you!")

# # # name=input('What is your name')
# # # age=input('What is your age')
# # # school=input('Where do you school')
# # # job=input('what do you  love')
# # # fav_meal=input('what is ur fav meal')

# # # print('A brief biography')
# # # print(f'I am called {name} and I am {age} years old.I school at {school} and I am a {job}. About food...I really love {fav_meal} ')

# # # temp_in_celcius = input('What is the temperature in celcius? ')
# # # temp_in_fahrenheit = (float(temp_in_celcius) * 9/5) + 32
# # # print(f'The temperature in Fahrenheit is {temp_in_fahrenheit}°F')

# # # # Interpolation Example
# # # name = 'JJ'   # Define a variable
# # # print(f"Hello, my name is {name}. Nice to meet you!")
# # # # name = input('What is your name? ')  # Get user input
# # # print(f"Hello, my name is {name}. Nice to meet you!")  # Print with interpolation

# # #string formatting
# # # Define variables
# # name = 'JJ'
# # age = 25
# # score = 95.5

# # #Method 1: f-strings (Python 3.6+ recommended like fill-in-the-blank)
# # print(f"My name is {name}, I am {age} years old, and my score is {score:.1f}.")

# # #Method 2: str.format() 
# # print("My name is {}, I am {} years old, and my score is {}.".format(name, age, score))

# # #Method 3: % formatting (older style)
# # print("My name is %s, I am %d years old." % (name, age))


# message = "Hello, DeepSeeds, Kilian, Paul!"
# print(message.split(','))  # Splits the string into a list 
# ['Hello', ' DeepSeeds!', ' Kilian', ' Paul!']

# # email = "user@example.com"

# # arr=[user, example.com]
# # arr[0]
# # arr[1]

# email= 'jj@gmail.com'
# if '@'in email and '.' in email:
#     username =email.split('@')[0]
#     domain= email.split('@')[1]
#     print(f'Username:{username}')
#     print(f'Domain: {domain}')

# else:
#     print('Invalid email format')   

# # Text analyzer
# text = "The quick brown fox jumps over the lazy dog"
# print(f"Text: {text}")
# print(f"Length: {len(text)} characters")
# print(f"Words: {len(text.split())} words")
# print(f"Uppercase: {text.upper()}")
# print(f"Title case: {text.title()}")
# print(f"Contains 'fox': {'fox' in text}")

#STRING EXERCISE
#Exercise 1: Name Formatter
full_name='jOhN dOe'
upper = full_name.title()
seperate = upper.split()
print('Exercise 1: Nmae Formatter')

print(f'Solution:{upper}')
print(f'First Name: {seperate[0]}')
print(f'Last Name: {seperate[1]}')
print('-'* 20)
print(''* 5)
# Or this can be done by formatting each character and later merging em



#Exercise 2: Word Counter
sentence = 'Python is an amazing programming language'
words = len(sentence.split())
total_chars = len(sentence)
number_of_a = sentence.count('a')


print('Exercise 2: Word Counter')
print(f'This sentence has {words} words.')
print(f'There are {total_chars} characters including spaces')
print(f'The letter \'a\' appears {number_of_a}times ')
print('-'* 20)
print(''* 5)

#Exercise 3: Simpler Cipher
print('Exercise 3: Simpler Cipher')
message = 'Hello'
chars = list(message) #here I have an array of each character in the word

ascii=[ord(char) for char in message]
print(ascii) #Here I just converted each character to its corresponding ascii value using the ord() function


cipher = [int + 1 for int in ascii]
print(cipher) #Here I just manipulated the ascii values by adding 1

coded_chars = [chr(int) for int in cipher]
print(coded_chars) #This converts the ascii numbers to theircorresponding characters

coded_word = ''.join(coded_chars)
print(coded_word) #Finally the coded or encrypted word