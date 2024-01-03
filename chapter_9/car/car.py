class Car:
    """Простая модель автомобиля."""

    def __init__(self, manufacturer, model, year):
        """Инициализируем атрибуты описания автомобиля."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Вывод отформатированного описания."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометре.
        При попытке обратной подкрутки изменение отклоняется."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Изменение пробега в меньшую сторону недопустимо.")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением"""
        self.odometer_reading += miles

    def read_odometer(self):
        """Выводит пробег машины в милях"""
        print(f"Данный автомобиль проехал миль: \n{self.odometer_reading}")


my_new_car = Car("audi", "m5", 2010)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(-10)
my_new_car.read_odometer()
