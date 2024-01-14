# 10.1. Изучение Python: откройте пустой файл в текстовом редакторе и напишите
# несколько строк текста о возможностях Python. Каждая строка должна начинаться
# с фразы «In Python you can…». Сохраните файл под именем learning_python.txt в
# каталоге, использованном для примеров этой главы. Напишите программу, которая
# читает файл и выводит текст три раза: с чтением всего файла, с перебором строк
# в списке с последующим выводом списка вне блока with.

with open("learning_python.txt") as lp:
    text = lp.read()
    print("1 Вывод")
    print(text)

with open("learning_python.txt") as lp:
    print("2 Вывод")
    lines = lp.readlines()
for line in lines:
    print(line.rstrip())

print("3 Вывод")
for line in lines:
    print(line.rstrip())
