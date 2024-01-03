# Больше условий: количество условий не ограничивается десятью. Попробуйте напи-
# сать другие условия и включить их в conditional_tests.py. Программа должна выдавать по
# крайней мере один истинный и один ложный результат для следующих видов проверок:
# • Проверка равенства и неравенства строк.
# • Проверки с использованием функции lower().
# • Числовые проверки равенства и неравенства, условий «больше», «меньше», «боль-
# ше или равно», «меньше или равно».
# • Проверки с ключевым словом and и or.
# • Проверка вхождения элемента в список.
# • Проверка отсутствия элемента в списке.

number = 1
text = 'Mouse'
test_list = ('bmw', 'lada', 'yamaha')
test_brand = 'lada'

print(number == 1, 'Выведет True')
print(number != 1, 'Выведет False')
print(text.lower() == 'mouse', 'Выведет True')
print(number >= 0, 'Выведет True')
print(number > 0, 'Выведет True')
print(number <= 0, 'Выведет False')
print(number < 0, 'Выведет False')
print(number == 1 and text.lower() == 'mouse', 'Выведет True')
print(number != 1 or text.lower() != 'mouse', 'Выведет False')
if test_brand in test_list:
    print('Lada в наличии')
brand = 'ural'
if brand in test_list:
    print(f'{brand} присутствует')
else:
    print(f'{brand} отсутствует')




