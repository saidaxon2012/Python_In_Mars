# import math 

# print("Universal dasturga xush kelibsiz!")
# print("Rejimni tanlang:")
# print("1 - Kalkulyator")
# print("2 - Matn tahlilchisi")

# choice = input("Rejim raqamini kiriting: ")

# if choice == "1":
#     a = int(input("Birinchi sonni kiriting: "))
#     b = int(input("Ikkinchi sonni kiriting: "))
    
#     amal = input("Amalni tanlang (+, -, *, /, sqrt): ")

#     if amal == "+":
#         print("Natija:", a + b)
#     elif amal == "-":
#         print("Natija:", a - b)
#     elif amal == "*":
#         print("Natija:", a * b)
#     elif amal == "/":
#         print("Natija:", a / b)
#     elif amal == "sqrt":
#         print(math.sqrt(a))
#         print(math.sqrt(b))
#     else:
#         print("Noto'g'ri amal tanlandi!")

# elif choice == "2":
#     text = input("Matn kiriting: ")
    
#     print("Matn uzunligi:", len(text))
#     print("Bo'sh joylar soni:", text.count(" "))
#     print("Katta harflar soni:", sum(1 for i in text if i.isupper()))
#     print("Katta harflarda:", text.upper())
#     print("Kichik harflarda:", text.lower())
#     print("Birinchi harf:", text[0])
#     print("Oxirgi harf:", text[-1])
#     print("Bo'sh joylar '_' bilan almashtirilgan:", text.replace(" ", "_"))
    
# else:
#     print("Noto'g'ri tanlov")
