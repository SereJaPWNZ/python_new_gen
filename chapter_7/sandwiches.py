# 7.8. Сэндвичи: создайте список с именем sandwich_orders, заполните его названиями
# различных видов сэндвичей. Создайте пустой список с именем finished_sandwiches. В цикле
# переберите элементы первого списка и выведите сообщение для каждого элемента (например,
# «I made your tuna sandwich»). После этого каждый сэндвич из первого списка перемещается
# в список finished_sandwiches. После того как все элементы первого списка будут
# обработаны, выведите сообщение с перечислением всех изготовленных сэндвичей.

sandwich_orders = ['тунцовый', 'куриный', 'ветчинный', 'сырный']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"Сэндвич {finished_sandwich} приготовлен")
    finished_sandwiches.append(finished_sandwich)
print("\nСписок готовых сэндвичей:")
for i in range(len(finished_sandwiches)):
    print(f'- {finished_sandwiches[i]}')
