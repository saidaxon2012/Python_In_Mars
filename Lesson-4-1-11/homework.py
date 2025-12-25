# # Exercise 1
a = input("Write something: ")
result = " "
for harf in a:
    if harf.isupper():
        result += "1"
    else:
        result += harf
print(result)

# Exercise 2
ex2_text = input("Write Something: ")
reversed_text = ""
for index in range(len(ex2_text)-1,-1,-1):
    reversed_text += ex2_text[index]
print(reversed_text)

# # Exercise 3
matn = input("Matn kiriting: ")
sonlar = ""
harflar = ""
for belgi in matn:
    if belgi.isdigit():
        sonlar += belgi
    else:
        harflar += belgi
print("Ajratilgan sonlar:", sonlar)
print("Qolgan matn:", harflar)

# # Exercise 4
a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
c = int(input("3-sonni kiriting: "))
d = int(input("4-sonni kiriting: "))
if a > b and a > c and a > d:
    big_num = a
elif b > a and b > c and b > d:
    big_num = b
elif c > a and c > d and c > b:
    big_num = c
else:
    big_num = d
print("Eng katta son:", big_num)

# # Exersice 5
son = input("Sonlar kiriting: ")
natija = {}
for raqam in son:
    if raqam.isdigit():
        natija[raqam] = natija.get(raqam, 0) + 1
for raqam, miqdor in natija.items():
    print(f"{raqam} raqami {miqdor} marta uchradi")

# # Exersice 6
sonlar = input("Sonlar kiriting: ")
royxat = sonlar.split()
royxat.sort()
print("Tartiblangan sonlar:", royxat)