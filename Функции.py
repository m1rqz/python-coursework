"""

money = int(input("Введите сумму денег: "))
while True:
    drink_price = int(input("Введите стоимость сока: "))
    bun_price = int(input("Введите стоимость булочки: "))
    if drink_price > 600 and bun_price > 600:
      break
    else:
        print("Ошибка: Сумма булочки и напитка должна быть больше 600 тг")
people = int(input("Количество людей: "))
if people < 1:
    people = 1
def lunch_balance(money, drink_price, bun_price, people=1):
    total_cost = (drink_price + bun_price) * people
    return money - total_cost
result = lunch_balance(money , drink_price , bun_price, people)
if result > 0:
    print(f"Останется {result} тенге")
elif result == 0:
    print("Хватает ровно!!!")
else:
    print(f"Не хватает {abs(result)} тенге")
if people > 2:
    print("В подарок шоколадка ) ")
if people > 2:
    print("Извините за шутку)))")

"""