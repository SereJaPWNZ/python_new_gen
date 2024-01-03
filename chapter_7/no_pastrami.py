# Без пастрами: используя список sandwich_orders из упражнения 7.8, проследите
# затем, чтобы значение 'pastrami' встречалось в списке как минимум три раза.
# Добавьте в начало программы код для вывода сообщения о том, что пастрами
# больше нет, и напишите цикл while для удаления всех вхождений 'pastrami' из
# sandwich_orders. Убедитесь в том, что в finished_sandwiches
# значение 'pastrami' не встречается ни одного раза.


sandwich_orders = ['тунцовый', 'pastrami', 'куриный', 'pastrami',
                   'ветчинный', 'сырный', 'pastrami']
finished_sandwiches = []
print('Pastrami больше нет')

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    finished_sandwich = sandwich_orders.pop()
    print(f"Сэндвич {finished_sandwich} приготовлен")
    finished_sandwiches.append(finished_sandwich)
print("\nСписок готовых сэндвичей:")
for i in range(len(finished_sandwiches)):
    print(f'- {finished_sandwiches[i]}')
