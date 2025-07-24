 #for loop
#1. starting point
#2. condition
#3. increment or decrement

names=['Will', 'JJ','Gita','Kilian','Paul', 'Mbom' 'jj mbom']
# for name in names:
count = 0
for name in names:
    print(f'{count + 1}. {name}')
    count += 1
    # if name.endswith('mbom'):
    #     print(f' We don catch you {name}')
    # else:
    #     print(f'welcome to the party : {name}')

#Range(stop)
for i in range(5):
    print(i)
#Range(start, stop)
for i in range(2, 7):
    print(i)

while True:
    print('madness')