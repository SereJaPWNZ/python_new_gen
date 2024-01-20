import json

username = input("Введите ваше имя:\n")
file_name = "username.json"
with open(file_name, "w") as fn:
    json.dump(username, fn)
    print(f"\nWe'll remember you when you come back, {username.title()}!")
