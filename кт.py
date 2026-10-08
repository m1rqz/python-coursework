
def can_add(total, amount):

    if (amount == 1 or amount == 2) and (total + amount <= 20):
        return True
    return False


def add_points(total, amount):

    return total + amount


def is_winner(total):

    return total == 20
def show_rules():

    print("\n" + "=" * 45)
    print("           ПРАВИЛА ИГРЫ «ГОНКА ДО 20»          ")
    print("=" * 45)
    print("1. Игра начинается с общего счёта 0.")
    print("2. Игрок и компьютер ходят по очереди.")
    print("3. Вы можете прибавить к счёту 1 или 2.")
    print("4. Компьютер всегда прибавляет 1.")
    print("5. Превышать 20 запрещено!")
    print("6. Кто первым получит ровно 20 — тот победил.")
    print("=" * 45 + "\n")


def read_choice(prompt, allowed):
    while True:

        user_input = input(prompt)

        if user_input in allowed:
            return user_input

        print("Ошибка! Выберите один из вариантов:", allowed)

def play_game():

    print("\n--- Новая игра началась! ---")


    total = 0

    while total < 20:
        print(f"Текущий счёт: {total}")


        while True:
            choice_str = read_choice(
                "Ваш ход (прибавить 1 или 2): ", ["1", "2"]
            )
            amount = int(choice_str)


            if can_add(total, amount):
                total = add_points(total, amount)
                print(f"Вы прибавили {amount}. Новый счёт: {total}")
                break
            else:
                print(f"Так ходить нельзя! Прибавив {amount}, счёт превысит 20.")

        #
        if is_winner(total):
            print("\n Поздравляем! Вы получили 20 и победили!")
            break


        print("\nХод компьютера...")
        comp_amount = 1
        total = add_points(total, comp_amount)
        print(f"Компьютер прибавил {comp_amount}. Новый счёт: {total}")

        # Проверка победы компьютера
        if is_winner(total):
            print("\n Компьютер получил 20 и выиграл партию!")
            break

    print("--- Игра завершена ---")
def main():

    while True:
        print("\n=== ГЛАВНОЕ МЕНЮ ===")
        print("1 - Начать")
        print("2 - Правила")
        print("0 - Выход")

        choice = read_choice("Выберите пункт меню: ", ["0", "1", "2"])

        if choice == "1":
            play_game()
        elif choice == "2":
            show_rules()
        elif choice == "0":
            print("\nСпасибо за игру! До свидания.")
            break


start_game = True

if start_game:
    main()
