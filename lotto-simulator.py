from random import shuffle


player_numbers = []
for i in range(6):
    while True:
        while True:
            try:
                number = int(input("Enter a number: "))
                break
            except ValueError:
                print("It's not a number!")
        if number not in player_numbers and 1 <= number <= 49:
            player_numbers.append(number)
            break
        else:
            print("""
            You already have entered the number
            or the number is smaller than 1 or bigger then 49
            """)
print(sorted(player_numbers))
lotto_numbers = [i for i in range(1, 50)]
shuffle(lotto_numbers)
lotto_numbers = lotto_numbers[:6]
print(sorted(lotto_numbers))
counter = 0
for number in player_numbers:
    if number in lotto_numbers:
        counter += 1
print(f"you have got {counter} number(s)")
