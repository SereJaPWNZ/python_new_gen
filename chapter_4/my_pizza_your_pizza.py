# Моя пицца, твоя пицца: начните с программы из упражнения 4.1. Создайте копию
# списка с видами пиццы, присвойте ему имя friend_pizzas. Затем сделайте следующее:
# • Добавьте новую пиццу в исходный список.
# • Добавьте другую пиццу в список friend_pizzas.
# • Докажите, что в программе существуют два разных списка. Выведите сообщение
# «My favorite pizzas are:», а затем первый список в цикле for. Выведите сообщение
# «My friend’s favorite pizzas are:», а затем второй список в цикле for. Убедитесь в том, что каждая новая пицца находится в соответствующем списке.

pizza_list = ["Pepperoni", "Margherita", "Vegetarian", "Quattro Formaggi"]

# Создаем копию списка
friend_pizzas = pizza_list[:]

# Добавляем новые пиццы в каждый из списков
pizza_list.append('Hawaiian')
friend_pizzas.append('BBQ Chicken')

# Вывод списка pizza_list:
print("My favorite pizzas are:")
for pizza in pizza_list:
    print(pizza)

# Вывод списка friend_pizzas:
print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)


