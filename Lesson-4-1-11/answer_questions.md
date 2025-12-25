1. Python’da o‘zgaruvchi (переменная) nima va u qanday yaratiladi?
# 1. Pythonda o'zgaruvchi biror ma'lumotni saqlaydi va uni har xil so'zlardan yaratish mumkin. Faqat qoidalarga roiya qilish zarur
2. int, float va str ma’lumot turlari bir-biridan nimasi bilan farq qiladi?
# int - butun son, float - o'nlik son, str - matn
3. input() funksiyasi nima qiladi va qanday turdagi ma’lumot qaytaradi?
# input funksiyasi foydalanuvchidan ma'lumot oladi. Input har doim str yani matn qaaytaradi
4. Type casting (tur o‘zgartirish) nima? Matnni son turiga o‘tkazish misolini yozing.
# Type castin bu biror bir ma'lumot turini boshqa ma'lumot turiga o'tkazish
# son = int(matn)
5. // operatori nima qiladi?
# Sonlarni bo'lib, butunini chiqarib beradi
6. math moduli nima uchun kerak? Undan 2 ta funksiyani nomlang.
# Matematik amallar bajarish uchun kerak
# print(math.pow(3,5))
# print(math.sqrt(8))
7. Matnni katta harflarga o‘tkazadigan string metodini yozing.
# .upper(), .title()
8. and va or mantiqiy operatorlari o‘rtasidagi farq nimada?
# and - Har ikki shart to‘g‘ri bo‘lsagina True qaytaradi
# or - Shartlardan kamida bittasi to‘g‘ri bo‘lsa True qaytaradi
9. True and False or True ifodasi qanday natija qaytaradi?
# True natijasini qaytaradi
10. if, elif, else yordamida oddiy shart konstruktsiyasi yozing.
# num = int(input("Raqam kirinting: "))
# if num > 5:
#    print("Raqam 5 dan kotta")
# elif num == 5:
#    print("Raqam 5 ga teng")
# else:
#    print("Raqam 5 dan kichiq")
11. Ichma-ich (вложенное) shart nima va qachon ishlatiladi?
# Ichma-ich shart (nested if) — bu if operatori ichida yana bir if operatorining ishlatilishi. Bu odatda murakkab shartlarni ketma-ket tekshirish kerak bo‘lganda qo‘llaniladi. Birinchi shart bajarilgandan keyin keyingi shartni tekshirish kerak bo‘lsa.
12. break va continue operatorlari nima qiladi? Ularning farqiga misol keltiring.
# break - Siklni to‘liq to‘xtatadi
# continue - to'xtamasdan keyingi shart o'tib ketadi. Davom etadi
# for i in range(5):
#    if i == 2:
#        break
#    print(i)
# for i in range(5):
#    if i == 2:
#        continue
#    print(i)
13. List (ro‘yxat) nima? Uni yaratishning turli usullarini ayting.
# List — bu bir nechta qiymatlarni bitta o‘zgaruvchida saqlashga mo‘ljallangan tartibli ma’lumotlar tuzilmasi.
# Kvatdat qavslar bilan, link() funsiyasi bilan va bo'sh ro'yxat bilan yaratish mumkin.
14. Ro‘yxatdagi elementga indeks orqali qanday murojaat qilinadi?
# Ro‘yxat elementlariga indeks orqali murojaat qilinadi. Indekslar 0 dan boshlanadi.
15. .append() metodi .insert() metodidan nimasi bilan farq qiladi?
# .append() - yangi elementni list oxiriga qo'shadi
# .insert() - yangi elementni xoxlagan joyga qo'yib beradi
16. Tuple nima va uning asosiy farqi listdan nimada?
17. Tuple ichidagi elementni o‘zgartirish mumkinmi? Nega?
18. Set (to‘plam) nima? Uning asosiy xususiyatlarini ayting.
19. Set ichidan elementni qanday o‘chirish mumkin?
20. Dictionary (lug‘at) nima va undan qiymatni kalit orqali qanday olish mumkin?
21. .get() metodi va dict[key] o‘rtasidagi farq nimada?
22. Dictionary'ga yangi kalit-qiymat juftligini qanday qo‘shish mumkin?
# person = {"name": "Ali", "age": 20}
# person["country"] = "Uzbekistan"
23. while sikli nima qiladi va qaysi holatlarda for o‘rniga qulayroq?
# while — berilgan shart TRUE bo‘lib turguncha kodni qayta-qayta bajaradigan sikl. Oldindan takrorlanish soni noma’lum bo‘lsa
24. Funksiya nima? Parametrlar va qaytariladigan qiymat nima uchun kerak?
# Funksiya — bu biror vazifani bajaradigan va qayta-qayta ishlatilishi mumkin bo‘lgan kod bloki. Parametrlar funksiyaga tashqaridan qiymat berish uchun kerak. Return funksiya bajarilgandan so‘ng natija berishi uchun ishlatiladi.
25. Type hinting nima va nima uchun ishlatiladi? Misol keltiring.
# def greeting(name: str) -> str:
#    return 'Hello, {}'.format(name)
# greeting(42)
