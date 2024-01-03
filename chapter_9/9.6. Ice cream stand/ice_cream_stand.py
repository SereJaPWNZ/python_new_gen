# 9.6. Киоск с мороженым: киоск с мороженым — особая разновидность ресторана.
# Напишите класс IceCreamStand, наследующий от класса Restaurant. Добавьте атрибут с именем
# flavors для хранения списка сортов мороженого. Напишите метод, который выводит этот список.
# Создайте экземпляр IceCreamStand и вызовите этот метод.

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


IceCreamStand = IceCreamStand("вьюга", "русской", ["яблочное", "персиковое", "гранатовое"])
IceCreamStand.display_flavors()
