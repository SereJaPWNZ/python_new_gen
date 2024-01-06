# 9.10. Импортирование класса Restaurant: возьмите последнюю версию класса Restaurant
# и сохраните ее в модуле. Создайте отдельный файл, импортирующий класс Restaurant.
# Создайте экземпляр Restaurant и вызовите один из методов Restaurant, чтобы показать,
# что команда import работает правильно.

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


class IceCreamStand(Restaurant):
    """Предоставляет аспекты ресторана, специфичные для киоска с мороженным."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Инициализируем родительские аргументы."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        """Выводит список сортов мороженного"""
        print("У нас доступны следующие виды мороженного: ")
        for flavor in self.flavors:
            print("-", flavor)
