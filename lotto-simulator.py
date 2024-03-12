from random import shuffle


def get_number_from_player():
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("It's not a number!")
    return number


def get_list_of_6_numbers_from_player():
    player_numbers = []
    for i in range(6):
        while True:
            number = get_number_from_player()
            if number not in player_numbers and 1 <= number <= 49:
                player_numbers.append(number)
                break
            else:
                print("""
                You already have entered the number
                or the number is smaller than 1 or bigger then 49
                """)
    return sorted(player_numbers)


def draw_6_lotto_numbers():
    lotto_numbers = [i for i in range(1, 50)]
    shuffle(lotto_numbers)
    lotto_numbers = lotto_numbers[:6]
    return sorted(lotto_numbers)


def show_winnings(player_numbers, lotto_numbers):
    counter = 0
    for number in player_numbers:
        if number in lotto_numbers:
            counter += 1
    return f"you have got {counter} number(s)"


player_numbers = get_list_of_6_numbers_from_player()
print(player_numbers)
lotto_numbers = draw_6_lotto_numbers()
print(lotto_numbers)
print(show_winnings(player_numbers, lotto_numbers))
