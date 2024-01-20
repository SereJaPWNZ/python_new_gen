# 10.12. Сохраненное любимое число: объедините две программы из
# упражнения 10.11 в один файл. Если число уже сохранено, сообщите
# его пользователю, а если нет — запросите любимое число пользователя
# и сохраните в файле. Выполните программу дважды, чтобы убедиться
# в том, что она работает.

import json
file_name = "number.json"


def asks_for_a_number():
    """Запрашивает число у пользователя и возвращает его."""
    number = input("Введите ваше любимое число:\n")
    return number


def save_number_to_file():
    """Сохраняет число в файл."""
    number = asks_for_a_number()
    with open(file_name, "w") as fn:
        json.dump(number, fn)


def get_stored_number():
    """Получает хранимое число, если оно существует."""
    try:
        with open(file_name, "r") as fn:
            number = json.load(fn)
    except FileNotFoundError:
        return None
    else:
        return number


def displays_the_recorded_number():
    """Читает значение из файла и выводит сообщение."""
    number = get_stored_number()
    if number:
        print(f"Я знаю ваше любимое число! Это {number}")
    else:
        save_number_to_file()
        number = get_stored_number()
        print(f"Я знаю ваше любимое число! Это {number}")


displays_the_recorded_number()
