# 9.15. Анализ лотереи: напишите цикл, который проверяет, насколько сложно выиграть
# в смоделированной вами лотерее. Создайте список или кортеж с именем my_ticket.
# Напишите цикл, который продолжает генерировать комбинации до тех пор, пока не выпадет
# выигрышная комбинация. Выведите сообщение с информацией о том, сколько выполнений
# цикла понадобилось для получения выигрышной комбинации.

import random

# Создание списка из 10 чисел и 5 букв
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
# Создание списка
my_ticket = ["1b3e", "2d7a", "3c9e"]


def gen_ticket(elements):
    # Случайным образом выбираем 4 элемента из списка
    select_4_elements_from_the_list = random.sample(elements, 4)
    # Преобразуем все элементы списка в строки
    convert_all_list_elements_to_strings = list(map(str, select_4_elements_from_the_list))
    get_ticket = ("".join(convert_all_list_elements_to_strings)).upper()
    return get_ticket


def hit_counter(my_ticket):
    counter = 0
    while True:
        generated_ticket = gen_ticket(elements).lower()
        counter += 1
        if generated_ticket in my_ticket:
            break
    return counter


print(hit_counter(my_ticket))
