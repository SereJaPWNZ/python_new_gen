# 9.4. Посетители: начните с программы из упражнения 9.1 (с. 175). Добавьте атрибут
# number_served со значением по умолчанию 0; он представляет количество обслуженных
# посетителей. Создайте экземпляр с именем restaurant. Выведите значение number_served,
# потом измените и выведите снова.
# Добавьте метод с именем set_number_served(), позволяющий задать количество
# обслуженных посетителей. Вызовите метод с новым числом, снова выведите значение.
# Добавьте метод с именем increment_number_served(), который увеличивает количество
# обслуженных посетителей на заданную величину. Вызовите этот метод с любым числом,
# которое могло бы представлять количество обслуженных клиентов, — скажем, за один день.

class Restaurant:
    """Простая модель ресторана"""

    def __init__(self, restaurant_name: str, cuisine_type: str):
        """Инициализация названия и кухни ресторана"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # количество обслуженных посетителей

    def describe_restaurant(self):
        """Выводит описание ресторана"""
        print(f"{self.restaurant_name.title()} c {self.cuisine_type} кухней.")

    def open_restaurant(self, open):
        """Выводит сообщение об открытии ресторана"""
        print(f'{self.restaurant_name.title()} был открыт в {open}.')

    def set_number_served(self, visitors_served: int):
        """Задает количество обслуженных посетителей."""
        if visitors_served >= self.number_served:
            self.number_served = visitors_served
        else:
            print("Количество посетителей не может быть меньше исходного значения.")

    def increment_number_served(self, up_visitors_served: int):
        """Увеличивает количество обслуженных посетителей на заданную величину."""
        self.number_served += up_visitors_served


restaurant = Restaurant("Chaika", "russian")
print("number serve:", restaurant.number_served)
restaurant.number_served = 10
print("number serve:", restaurant.number_served)
restaurant.set_number_served(10)
print("number serve:", restaurant.number_served)
restaurant.increment_number_served(50)
print("number serve:", restaurant.number_served)
