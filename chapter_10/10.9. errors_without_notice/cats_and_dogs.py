# 10.9. Ошибки без уведомления: измените блок except из упражнения 10.8 так, чтобы при
# отсутствии файла программа продолжала работу, не уведомляя пользователя о проблеме.

try:
    with open("dogs.txt") as d:
        alias_dogs = d.readlines()
    print("Список кличек собак:")
    for alia in alias_dogs:
        print(alia.title().rstrip())
    print("\nСписок кличек кошек:")
    with open("cats.txt") as c:
        alias_cats = c.readlines()
    for alia in alias_cats:
        print(alia.title().rstrip())

except FileNotFoundError:
    pass
