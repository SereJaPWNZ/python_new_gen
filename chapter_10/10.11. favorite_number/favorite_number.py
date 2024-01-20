# 10.11. Любимое число: напишите программу, которая запрашивает у пользователя
# его любимое число. Воспользуйтесь функцией json.dump() для сохранения этого
# числа в файле. Напишите другую программу, которая читает это значение и выводит
# сообщение: «Я знаю ваше любимое число! Это _____».

import json


def asks_for_a_number():
    """Запрашивает число у пользователя и возвращает его."""
    number = input("Введите ваше любимое число:\n")
    return number


def save_number_to_file():
    """Сохраняет число в файл."""
    number = asks_for_a_number()
    file_name = "number.json"
    with open(file_name, "w") as fn:
        json.dump(number, fn)


def displays_the_recorded_number():
    """Читает значение из файла и выводит сообщение."""
    file_name = "number.json"
    with open(file_name, "r") as fn:
        number = json.load(fn)
    print(f"Я знаю ваше любимое число! Это {number}")


save_number_to_file()
displays_the_recorded_number()
