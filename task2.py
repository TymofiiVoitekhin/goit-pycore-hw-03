import random
import time

def get_numbers_ticket (min, max, quantity):
    all_numbers = []
# Створення загального списку всіх значень
    for i in range (min, max):
        all_numbers.append(i)

    list_numbers = ()
# Перебір списку, поки не створиться унікальний
    while len(list_numbers) != quantity:
        list_numbers_random = random.choices (all_numbers, k=quantity)
        set_list = set(list_numbers_random)
        list_numbers = sorted(set_list)

    return(list_numbers)
# Введення значень користувачем
min = int(input("Введіть мінмальне значення (більше 1): "))
max = int(input("Введіть максимальне значення (менше 1000): "))
quantity = int(input("Введіть кількість чисел: "))

start = time.perf_counter()

if min >= 1 and max <=1000:
    result = get_numbers_ticket (min, max, quantity)
    print("Ваші лотерейні числа: ", result)
else:
     print("Значення не відповідає вимогам")

end = time.perf_counter()
print("Час виконання:", end - start, "секунд")