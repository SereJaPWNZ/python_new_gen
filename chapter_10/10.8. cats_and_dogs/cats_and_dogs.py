# 10.8. Кошки и собаки: создайте два файла с именами cats.txt и dogs.txt.
# Сохраните по крайней мере три клички кошек в первом файле и три клички
# собак во втором. Напишите программу, которая пытается прочитать эти файлы
# и выводит их содержимое на экран. Заключите свой код в блок try-except
# для перехвата исключения FileNotFoundError и вывода понятного сообщения
# об отсутствии файла. Переместите один из файлов в другое место файловой
# системы; убедитесь в том, что код блока except выполняется как положено.

try:
    dogs = "dogs.txt"
    cats = "cats.txt"

    with open(dogs) as d:
        alias_dogs = d.readlines()
    print("Список кличек собак:")
    for alia in alias_dogs:
        print(alia.title().rstrip())
    print("\nСписок кличек кошек:")
    with open(cats) as c:
        alias_cats = c.readlines()
    for alia in alias_cats:
        print(alia.title().rstrip())

except FileNotFoundError:
    print("Файл cats.txt и/или dogs.txt отсутствует")
