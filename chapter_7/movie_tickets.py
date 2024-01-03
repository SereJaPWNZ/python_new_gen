# 7.5. Билеты в кино: кинотеатр установил несколько вариантов цены на билеты
# в зависимости от возраста посетителя. Для посетителей младше 3 лет билет бесплатный; в возрасте
# от 3 до 12 билет стоит $10; наконец, если возраст посетителя больше 12, билет стоит $15.
# Напишите цикл, который предлагает пользователю ввести возраст и выводит цену билета.

while True:
    age = input('Введите ваш возраст: \n(Для завершения программы введите "quit")\n')
    if age.lower() == 'quit':
        break
    age = int(age)
    if age < 3:
        print('билет бесплатный')
    elif age < 12:
        print('Стоимость билета $10')
    else:
        print('Стоимость билета $15')
    print()
