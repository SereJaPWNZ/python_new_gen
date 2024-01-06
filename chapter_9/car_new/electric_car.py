from car import Car


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


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, manufacturer, model, year):
        """Инициализирует атрибуты класса-родителя.
        Затем инициализирует атрибуты, специфические для электромобиля."""
        super().__init__(manufacturer, model, year)
        self.battery = Battery()
