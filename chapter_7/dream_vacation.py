# 7.10. Отпуск мечты: напишите программу, которая опрашивает пользователей, где бы они
# хотели провести отпуск. Включите блок кода для вывода результатов опроса.

answers = {}
active = True
while active:
    print('\nДля завершения программы введите "quit" в любом из полей ввода.')
    name = input('Введите ваше имя: ')
    if name.lower() == 'quit':
        active = False
        continue
    location = input('Введите место, где бы вы хотели провести отпуск: ')
    if location.lower() == 'quit':
        active = False
        continue
    answers[name] = location
if answers:
    print('\nРезультаты опроса:')
    for name, answer in answers.items():
        print(f'- {name.title()} хочет отдохнуть в {answer.title()}.')
