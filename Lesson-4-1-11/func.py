def hisobla(a,b):
    plus = a + b
    minus = a - b
    multiply = a * b
    divided = a / b
    # print(f"{a} + {b} = {a + b}")
    # print(f"{a} - {b} = {a - b}")
    # print(f"{a} * {b} = {a * b}")
    # print(f"{a} / {b} = {a / b}")
    return {
        "plus" : plus,
        "minus" : minus,
        "multiply" : multiply,
        "divided" : divided
    }

result = hisobla(43, 76)
print(result["divided"])

