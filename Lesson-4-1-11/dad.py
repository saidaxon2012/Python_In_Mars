products = [
    {
        "id": 1,
        "name": "Non",
        "price": 3000
    },
    {
        "id": 2,
        "name": "Qaymoq",
        "price": 15000
    }
]

print("Mahsulotlar ro'yxati:\n**********************")
for product in products:
    print(f"{product['id']}. {product['name']} - {product['price']} so'm")

choice = int(input("Mahsulot ID raqamini kiriting: "))

choosen_product = {}
for product in products:
    if product["id"] == choice:
        choosen_product = product

print(f"Siz {choosen_product['name']}ni tanladingiz. Narxi: {choosen_product['price']}")

cash = int(input("To'lov summasini kiriting: "))
cashback = cash - choosen_product["price"]
if cashback == 0:
    print(f"Siz {choosen_product['name']} sotib oldingiz")
elif cashback > 0:
    print(f"Siz {choosen_product['name']} sotib oldingiz va {cashback} so'm qaytim olasiz")
else: 
    print(f"Siz {choosen_product['name']} sotib olish uchun yana {cashback * (-1)} so'm to'lashingiz kerak")