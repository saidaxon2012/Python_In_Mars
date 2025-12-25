fruits = ['apple', 'banana', 'mini orange', 'kiwi', 'watermelon', 'pineapple', 'strawberry', 'blueberry', 'limon']

for i, g in enumerate(fruits):
    if i % 2 == 0: 
        print(f'{i} - {g}')
    else:
        print(f'{i} element deleted')
        fruits.pop(i)
print(fruits)