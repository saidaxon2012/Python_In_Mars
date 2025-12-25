# list

# collections - 4

# 1 - list
# 2 - tuple
# 3 - set
# 4 - dictionary

name = ['John', 'Jack', 'Joe', 'Sam', 'Bob', 'Sally']
print(name)
print(type(name))
print(name[0])
print(len(name))
print(name[5])
print(name[-1])
print(name[0:3])
print(name[2:5])
print(name[::-1])

# methods
fruits = []
fruits = list()
print(fruits)
fruits.append('apple')
print(fruits)
fruits.append('banana')
print(fruits)
fruits.insert(1, 'mini orange')
print(fruits)

# удаление элемента

fruits = ['apple', 'banana', 'mini orange', 'grape']
fruits.pop()
print(fruits)
fruits.remove('banana')
print(fruits)

print(fruits)
fruits = ['apple', 'banana', 'mini orange', 'grape']
print(fruits)
amount = int(input('Enter amount of fruits to add: '))
for i in range(amount):
    nameOfFruits = input('Enter the name of the fruit: ')
    fruits.append(nameOfFruit)
    print(f'{nameOfFruit} added to list fruits')
print(fruits)
for i in fruits:
    print(i)