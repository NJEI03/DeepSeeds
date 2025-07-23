# print('Hello DeepSeeds yo')
# name= 'JJ'

# print("Hello I am called " + name + ". Nice to meet you!")

name=input('What is your name')
age=input('What is your age')
school=input('Where do you school')
job=input('what do you  love')
fav_meal=input('what is ur fav meal')

print('A brief biography')
print(f'I am called {name} and I am {age} years old.I school at {school} and I am a {job}. About food...I really love {fav_meal} ')

temp_in_celcius = input('What is the temperature in celcius? ')
temp_in_fahrenheit = (float(temp_in_celcius) * 9/5) + 32
print(f'The temperature in Fahrenheit is {temp_in_fahrenheit}°F')