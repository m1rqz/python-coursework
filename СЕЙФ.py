print("=" * 40)
print("     Cистема безопастности: Взлом")
print("=" * 40)
print("Агент,вам нужно пройти 3 уровня защиты")
print("Будьте осторожны: ошибиться нельзя!")
low = 1
high = 100
max_attempts = 3
level1_passed = False
for attempt in range(1, max_attempts + 1):
    secret_code = (low + high)  //2
    print("Попытка", attempt, "из", max_attempts)
    user_input = input("Введите число: ")
if not user_input.isdigit():
    print("Ошибка! Нужно ввести целое число.")
    continue
guess = int(user_input)
if guess == secret_code:
    print("КОД ВЕРНЫЙ!")
    print("УРОВЕНЬ 1 ПРОЙДЕН!")
    level1_passed = True
    break
elif guess < secret_code:
    print("Загадоное число больше.")
    low = secret_code + 1
else:
    print("Загадоное число меньше.")
    high = secret_code - 1
if not level1_passed:
    print("ТРЕВОГА! Система заюлокирована. Попытки исчерпаны.")
    is_active = False