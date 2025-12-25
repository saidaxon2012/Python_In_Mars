notes = []
note_choice = ['Note list', 'Create note', 'Remove note', 'Quit'] 

while (True):
    print("\n --- Asosiy menu ---")
    for raqam, choice in enumerate(note_choice, start=1):
        print(f"{raqam}. {choice}")
        
    choice = int(input("Tanlovni kiriting: "))

    if choice == 1:
        if len(notes) == 0:
            print("Hozircha notelar yo'q")
        else:
            print("\n --- NOTElar ro'yxati ---")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")    
    elif choice == 2:
        count = int(input("Nechta note yaratmoqchisiz: "))
        for i in range(count):
            new_note = input("Note matnini kiriting: ")
            notes.append(new_note)
        print("Notelar qo'shildi!")
        print(notes)
    elif choice == 3:
        if len(notes) == 0:
            print("Hozircha notelar yo'q")
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")    
        remove = int(input("Qaysi note o'chiriladi (raqam kiriting): " ))-1
        if remove >= len(notes):
            print("Bunday note yo'q")
        else:
            removed_item = notes.pop(remove)
            print(f"Quyidagi note o'chirildi. \n {removed_item}")
            
    elif choice == 4:
        print("Dastur yakunlandi.")
        if len(notes) > 0:
            print("Notelar ro'yxati\n")
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")
        break
    else:
        print("Noto'g'ri tanlov!")