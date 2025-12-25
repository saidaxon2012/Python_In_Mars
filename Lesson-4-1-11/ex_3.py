ism = input("Ismingizni kiriting: ")
telefon = input("Telefon raqamingizni kiriting: ")
address = input("Adresingizni kiriting: ")

print("\nO'zgartirish uchun bo'limni tanlang:")
print("1 - Ismni o'zgartirish")
print("2 - Telefon raqamni o'zgartirish")
print("3 - Addresni o'zgartirish")

tanlov = input("Tanlovingiz (1/2/3): ")

if tanlov == "1":
    ism = input("Yangi ismni kiriting: ")

elif tanlov == "2":
    telefon = input("Yangi telefon raqamni kiriting: ")

elif tanlov == "3":
    address = input("Yangi addresni kiriting: ")

else:
    print("Noto'g'ri tanlov kiritildi!")

print("\n--- Yangilangan ma'lumotlar ---")
print("Ism:", ism)
print("Telefon:", telefon)
print("Addres:", address)