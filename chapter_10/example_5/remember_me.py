import json


# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.

def great_user():
    """Выводит приветствие"""
    try:
        with open("username.json") as un:
            username = json.load(un)
    except FileNotFoundError:
        username = input("Введите ваше имя:\n")
        file_name = "username.json"
        with open(file_name, "w") as fn:
            json.dump(username, fn)
            print(f"\nWe'll remember you when you come back, {username.title()}!")
    else:
        print(f"Welcome back, {username.title()}!")


great_user()
