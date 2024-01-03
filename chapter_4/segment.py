# Сегменты: добавьте в конец одной из программ, написанных в этой главе, фрагмент,
# который делает следующее:
# •
# Выводит сообщение «The first three items in the list are:», а затем использует сегмент
# для вывода первых трех элементов из списка.
# •
# Выводит сообщение «Three items from the middle of the list are:», а затем использует
# сегмент для вывода первых трех элементов из середины списка.
# •
# Выводит сообщение «The last three items in the list are:», а затем использует сегмент
# для вывода последних трех элементов из списка.


players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(f'The first three items in the list are:\n{players[:3]}')
middle_index = len(players) // 2
print(f'Three items from the middle of the list are:\n{players[(middle_index-1):(middle_index+2)]}')
print(f'The last three items in the list are:\n{players[-3:]}')
