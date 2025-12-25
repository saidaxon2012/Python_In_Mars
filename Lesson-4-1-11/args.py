# # # # args and kwargs

# # # def sumNums(a, b, c):
# # #     return a + b + c

# # # print(sumNums(10, 20, 30))

# # # *args

# def add_number(*args):
#     print(type(args))
#     return sum(args)

# result = add_number(1, 10, 20)
# print(add_number(1, 2))
# print(add_number(1, 2, 3, 4, 5, 6, 7, 10))
# print(type(result))

# # # # **kwargs
# def print_user(**kwargs):
#     for key, value in kwargs.items():
#         print(key, value)
# print_user(name='Alex', age = 23, city='London')

# def example(a, b, *args, **kwargs):
#     print(a, b)
#     print(args)
#     print(kwargs)
    
# example(1, 2, 3, 4, x=10, y=20)

# students = ['John', 'Alex', 'Jake']
# print(type(students))
# print(students)
# students[0] = 'Samir'
# print(students)

# students = ('John', 'Alex', 'Jake', 'John')
# print(type(students))
# print(students)
# students[0] = 'Samir'
# print(students)

# views.py
# def index(request, pk=pk,)

def register_user(username, email, **kwargs):
    print(f"Username: {username}")
    print(f"Email: {email}")
    
    if not kwargs:
        print("No additional data")
    else:
        print("Additional data:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")