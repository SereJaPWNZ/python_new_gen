# 9.9. Обновление аккумулятора: используйте окончательную версию программы
# electric_car.py из этого раздела. Добавьте в класс Battery метод с именем upgrade_battery().
# Этот метод должен проверять размер аккумулятора и устанавливать мощность равной 100, если
# она имеет другое значение. Создайте экземпляр электромобиля с аккумулятором по умолчанию,
# вызовите get_range(), а затем вызовите get_range() во второй раз после вызова
# upgrade_battery(). Убедитесь в том, что запас хода увеличился.

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
        long_name = (f"Год выпуска автомобиля: {self.year}"
                     f"\nМарка автомобиля: {self.manufacturer.title()}"
                     f"\nМодель автомобиля: {self.model.title()}")
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


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, manufacturer, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля."""
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Выводит информацию, что у электромобиля нет бензобака."""
        print("This car doesn't need a gas tank!")


class Battery:
    """Простая модель аккумулятора электромобиля."""

    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"У данной машины мощность батареи {self.battery_size}-kWh.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            save_the_move = 260
        elif self.battery_size == 100:
            save_the_move = 315

        print(f"This car can go about {save_the_move} miles on a full charge.")


my_tesla = ElectricCar("tesla", "x", 2015)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
