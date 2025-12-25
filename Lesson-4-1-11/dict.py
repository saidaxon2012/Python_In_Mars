# # dict in Python

# user = {
#     'name': 'John',
#     'age': 33,
#     'salary': 39000
# }

# print(user['name'], user['age'])

# # add items

# user['city'] = 'London'
# print(user)

# # remove salary 
# user.pop('salary')
# print(user)
# user['age'] = 28
# print(user)

# # for key, value in user.items():
# #   print(key, value)
# print(user.keys())
# print(user.values())
# print(user.items())

users = dict()
print(users)
print(type(users))
for i in range(3):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    grade = int(input("Enter your grade: "))
