# 9.1. Ресторан: создайте класс с именем Restaurant. Метод __init__() класса Restaurant
# должен содержать два атрибута: restaurant_name и cuisine_type. Создайте метод describe_
# restaurant(), который выводит два атрибута, и метод open_restaurant(), который выводит
# сообщение о том, что ресторан открыт.
# Создайте на основе своего класса экземпляр с именем restaurant. Выведите два атрибута
# по отдельности, затем вызовите оба метода.

class Restaurant:
    """Простая модель ресторана"""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализация названия и кухни ресторана"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Выводит описание ресторана"""
        print(f"{self.restaurant_name.title()} c {self.cuisine_type} кухней.")

    def open_restaurant(self, open):
        """Выводит сообщение об открытии ресторана"""
        print(f'{self.restaurant_name.title()} был открыт в {open}.')


my_restaurant = Restaurant("вьюга", "русской")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant(open=1960)
