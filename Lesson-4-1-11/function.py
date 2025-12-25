# def functionName(arguments):
#     code of function(body of function)
    
# def add(a, b):
#     print(a + b)

# add(20, 33)
# add(33, 99)
expenses = [10000, 43000, 31000, 44000, 9000, 98000]
expenses2 = [14000, 26000, 76000, 24000, 1000, 8000]
expenses3 = [76000, 32000, 87000, 94000, 89000, 28000]

def sumOfList(list):
    result = 0 
    for i in list:
        result += 1
    print(result)

sumOfList(expenses)
sumOfList(expenses2)
sumOfList(expenses3)

# function for palindrome
def is_palindrome(text):
    if text == text[::-1]:
        print("Da palindrome")
    else:
        print("Adashdin")