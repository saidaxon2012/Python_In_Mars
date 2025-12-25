# studentList = list()
# count = int(input("Nechta student bor?"))
# for i in range(count):
#     name = input(f'Enter {i+1} name: ')
#     age = input(f'Enter {name}s age: ')
#     salary = input(f'Enter {name}s salary: ')
#     new_student = dict()
#     new_student['name'] = name
#     new_student['age'] = age
#     new_student['salary'] = salary
#     studentList.append(new_student)
#     print(f'{name} added to Student List!')
# print(studentList)


# while Loop
while True:
    num1 = int(input('Enter first number or 0 to quit: '))
    if num1 == 0:
        print("Siz darsturni yopdiz!")
        break
    else:
        operator = input("Enter operator: + - / * : ")
        num2 = int(input("Enter second number: "))
        if operator == '+':
            result = num1 + num2
            print(f'{num1} {operator} {num2} = {result}')
        elif operator == '-':
            result = num1 - num2
            print(f'{num1} {operator} {num2} = {result}')
        elif operator == '/':
            result = num1 / num2
            print(f'{num1} {operator} {num2} = {result}')
        elif operator == '*':
            result = num1 * num2
            print(f'{num1} {operator} {num2} = {result}')