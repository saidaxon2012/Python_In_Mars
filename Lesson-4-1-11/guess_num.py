# guess the number

# def choose_defficulty():
#     print("Choose level of difficulty: ")
#     print("1. Easy (1-50, 10 attempts)")
#     print("2. Medium (1-100, 7 attempts)")
#     print("3. Hard (1-500, 5 attempts)")

#     while True:
#         choice = input("\nYour choice (1/2/3): ").strip()
#         if choose == '1':
#             return 50, 10, 'Easy'
#         elif choice == '2':
#             return 100,7, 'Medium'
#         elif choice == '3':
#             return 500, 5, 'Hard'
#         else:
#             print("Xato. 1, 2, 3 tanlang")
# choose_difficulty()

def get_player_guess(min_num, max_num):
    while True:
        try:
            guess = int(input(f'Your guess ({min_num} - {max_num}): '))
            if min_num <= guess <= max_num:
                return guess
            else: 
                print(f'Number should be from {min_num} to {max_num}')
        except Exception as e:
            print(f'Error: {e}')
            
print(get_player_guess(6, 66))