products = ["Non", "Cola", "Cookies", "Candies", "Snacks", "Milka"]
for raqam, product in enumerate(products):
    print(f"{raqam+1}. {product}")

p_1 = int(input("Mahsulotni tanlang: "))
if p_1 == 1:
    print("Siz nonni tanladingiz.")
    narx = int(input("Nonning narxi 3000 so'm. Pulni kiriting: "))
    if narx == 3000:
        print("Non sotib oldingiz.")
    elif narx > 3000:
        qaytim = narx - 3000
        print(f"{qaytim} qaytimingiz.")
    else:
        print("Mablag' yetarli emas.")
if p_1 == 2:
    print("Siz colani tanladingiz.")
    narx = int(input("Colaning narxi 18000 so'm. Pulni kiriting: "))
    if narx == 18000:
        print("Cola sotib oldingiz.")
    elif narx > 18000:
        qaytim = narx - 18000
        print(f"{qaytim} qaytimingiz.")
    else:
        print("Mablag' yetarli emas.")
if p_1 == 3:
    print("Siz cookiesni tanladingiz.")
    narx = int(input("Cookiesning narxi 20000 so'm. Pulni kiriting: "))
    if narx == 20000:
        print("Cookies sotib oldingiz.")
    elif narx > 20000:
        qaytim = narx - 20000
        print(f"{qaytim} qaytimingiz.")
    else:
        print("Mablag' yetarli emas.")
if p_1 == 4:
    print("Siz candiesni tanladingiz.")
    narx = int(input("Candiesning narxi 5000 so'm. Pulni kiriting: "))
    if narx == 5000:
        print("Candies sotib oldingiz.")
    elif narx > 5000:
        qaytim = narx - 5000
        print(f"{qaytim} qaytimingiz.")
    else:
        print("Mablag' yetarli emas.")
if p_1 == 5:
    print("Siz snacksni tanladingiz.")
    narx = int(input("Snacksning narxi 10000 so'm. Pulni kiriting: "))
    if narx == 10000:
        print("Snacks sotib oldingiz.")
    elif narx > 10000:
        qaytim = narx - 10000
        print(f"{qaytim} qaytimingiz.")
    else:
        print("Mablag' yetarli emas.")
if p_1 == 6:
    print("Siz milkani tanladingiz.")
    narx = int(input("Milkaning narxi 15000 so'm. Pulni kiriting: "))
    if narx == 15000:
        print("Milka sotib oldingiz.")
    elif narx > 15000:
        qaytim = narx - 15000
        print(f"{qaytim} qaytimingiz.")
    else:
        print("Mablag' yetarli emas.")
