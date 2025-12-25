# Lambda functions

def add(a,b):
    return a + b

result = add(10, 20)
print(result)

# # # lambda argument: statement
add = lambda a,b: a + b
print(add(10, 20))
add = lambda x: x ** 2
print(square(12))

# # # if else

max = lambda a,b: a if a > b else b
print(max(10, 5))

# # # map
nums = [1, 2, 3, 4]
result = list(map(lambda x: x ** 2))
print(result)
# nums_squared = [1, 4, 9, 16]

# filter
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x * 2, nums))
print(result)
# nums_squared = [1, 4, 9, 16]

# filter
nums = [1, 2, 3, 4, 5 ]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)
print(odd)
# reduce
from functools import reduce
nums = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a + b, nums)
print(result)
