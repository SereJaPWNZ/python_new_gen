# 10.13. Проверка пользователя: последняя версия remember_me.py
# предполагает, что пользователь либо уже ввел свое имя, либо
# программа выполняется впервые. Ее нужно изменить на тот случай,
# если текущий пользователь не является тем человеком, который
# последним использовал программу. Прежде чем выводить приветствие
# в greet_user(), спросите, правильно ли определено имя пользователя.
# Если ответ будет отрицательным, вызовите get_new_username()
# для получения правильного имени пользователя.

import json


# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.

def get_stored_username():
    """Получает хранимое имя пользователя, если оно существует."""
    file_name = "username.json"
    try:
        with open(file_name) as fn:
            username = json.load(fn)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя"""
    username = input("Введите ваше имя:\n")
    file_name = "username.json"
    with open(file_name, "w") as fn:
        json.dump(username, fn)
        return username


def great_user():
    """Приветствует пользователя по имени."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username.title()}!")
    else:
        username = get_new_username()
        print(f"\nWe'll remember you when you come back, {username.title()}!")


great_user()
