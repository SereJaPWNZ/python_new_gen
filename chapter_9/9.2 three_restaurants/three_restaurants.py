# 9.2 Три ресторана: начните с класса из упражнения 9.1. Создайте три разных экземпляра,
# вызовите для каждого экземпляра метод describe_restaurant().

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


r_viuga = Restaurant('viuga', 'russian')
r_sssr = Restaurant('SSSR', 'russian')
r_taito = Restaurant('taito', 'japanese')

r_taito.describe_restaurant()
r_viuga.describe_restaurant()
r_sssr.describe_restaurant()
