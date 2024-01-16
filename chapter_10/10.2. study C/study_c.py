# 10.2. Изучение C: метод replace() может использоваться для замены любого слова в стро-
# ке другим словом. В следующем примере слово 'dog' заменяется словом 'cat':
# >>> message = "I really like dogs."
# >>> message.replace('dog', 'cat')
# 'I really like cats.'
# Прочитайте каждую строку из только что созданного файла learning_python.txt и замените
# слово Python названием другого языка, например C. Выведите каждую измененную строку
# на экран.

with open("learning_python.txt") as lp:
    messages = lp.readlines()

for message in messages:
    new_message = message.replace("Python", "C")
    print(new_message.rstrip())

