 #for loop
#1. starting point
#2. condition
#3. increment or decrement

# names=['Will', 'JJ','Gita','Kilian','Paul', 'Mbom' 'jj mbom']
# # for name in names:
# count = 0
# for name in names:
#     print(f'{count + 1}. {name}')
#     count += 1
#     # if name.endswith('mbom'):
#     #     print(f' We don catch you {name}')
#     # else:
#     #     print(f'welcome to the party : {name}')

# #Range(stop)
# # for i in range(5):
# #     print(i)
# # #Range(start, stop)
# # for i in range(2, 7):
# #     print(i)

# count =1
# while count <= 5:

#     print(f'Count is:{count}')
#     count += 1

#     user_input = ''
#     while user_input != 'quit':
#         user_input = input('Enter "quit" to exit: ')

#         if user_input!= 'quit':
#          print(f'You have entered:{user_input}')
#         else:
#          print('Exiting the loop...')

# print('Goodbye!')

#Break existing loop completely
print('Finding the first even number:')
for number in range(1,10):
    if number % 2 ==0:
        print(f'Found even number:{number}')
        break
    print(f'{number} is odd')

#Continue - skip next iteration
print('\nPrinting only odd numbers')
for number in range(1,10):
    if number % 2 == 0:
        continue # skip even numbers
    print(f'Odd number: {number}') 