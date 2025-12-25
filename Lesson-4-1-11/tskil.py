# for loop

# for variable in range(a, b, c):
#     code of the loop
    
# a - start
# b - end
# c - step

for i in range(1, 4+1):
    print(i)
    
total = 0
amount = int(input("Enter amount of expenses: "))
for i in range(amount):
    expenses = int(input(f'Enter {i+1} expenses: '))
    totel = total + expenses
print(total)

num = int(input("Enter number for multiplication table: "))
for i in range(1,11):
    print(f'{num} * {i} = {num*i}')