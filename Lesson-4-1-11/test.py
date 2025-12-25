schedule_teacher = [
    ['English', 'Math', 'History', 'Biology'],
    ['PI', 'IT', 'Physics', 'Russian'],
    ['English', 'History', 'Chemistry'],
    # ['PJ', 'Math', 'Geography', 'Mother tongue'],
    # ['Fine arts', 'Math', 'Russian', 'World history']
]
day = int(input("Kunni kiriting (1-3):"))
print(f"Bu kuni ustozda {len(schedule_teacher[day-1])} ta dars bor.")
chooseHour = int(input("Qaysi darsda qoshimcha dars berishini xohlaysiz: "))
if chooseHour <= len(shcedule_teacher[day-1]) and chooseHour > 0:
    print(f"Ustoz {schedule_teacher[day-1][chooseHour-1]} darsini beradi.")
    print("Mumkin emas")
else:
    print(f"Ushbu dars vaqti mavjud emas. Qoshimcha dars beriladi.")