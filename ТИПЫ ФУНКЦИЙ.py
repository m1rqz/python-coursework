
"""
def  entry_messeg (group):
    if group == "T118":
        return "T118: Вход рашрешен"
    return "Обратитесь к Куратору"
check_entry = entry_messeg
print(check_entry("T118"))
print(check_entry("T119"))
print(check_entry("т118"))
print(check_entry(""))
print(type(check_entry))
print(type(check_entry("T118")))

"""

""""
def standard_fare(km):
    return 500 + 100 *km
def student_fare(km):
    return 300+ 70 * km
def trip_cost(km, tariff):
    return tariff(km)
print(trip_cost(10,standard_fare))
print(trip_cost(10,student_fare))

print(trip_cost(0,standard_fare))
print(trip_cost(0,student_fare))

print(trip_cost(1, standard_fare))
print(trip_cost(1, student_fare))

"""


def make_discount(amount):
    def discount(price):
     result = price - amount
     if result < 0:
         return 0
     return result
    return discount
discount_100 = make_discount(100)
discount_300 = make_discount(300)

print(discount_100(250))
print(discount_300(250))

discount_0 = make_discount(0)
print(discount_0(500))

print(discount_100(99))
print(discount_100(101))



