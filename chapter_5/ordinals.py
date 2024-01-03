# Порядковые числительные: порядковые числительные в английском языке заканчи-
# ваются суффиксом th (кроме 1st, 2nd и 3rd).
# • Сохраните числа от 1 до 9 в списке.
# • Переберите элементы списка.
# • Используйте цепочку if-elif-else в цикле для вывода правильного окончания чис-
# лительного для каждого числа. Программа должна выводить числительные "1st 2nd
# 3rd 4th 5th 6th 7th 8th 9th", причем каждый результат должен располагаться в от-
# дельной строке.

numbers = [number for number in range(1, 10)]
ordinals = ''
for number in numbers:
    if number == 1:
        print(f'{number}' + 'st')
    elif number == 2:
        print(f'{number}' + 'nd')
    elif number == 3:
        print(f'{number}' + 'rd')
    else:
        print(f'{number}' + 'th')
