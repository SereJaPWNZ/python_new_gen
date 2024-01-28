# 11.3. Работник: напишите класс Employee, представляющий работника.
# Метод __init__() должен получать имя, фамилию и ежегодный оклад;
# все эти значения должны сохраняться в атрибутах. Напишите метод
# give_raise(), который по умолчанию увеличивает ежегодный оклад
# на $5000 — но при этом может получать другую величину прибавки.
# Напишите тестовый сценарий для Employee. Напишите два тестовых
# метода, test_give_default_raise() и test_give_custom_raise().
# Используйте метод setUp(), чтобы вам не приходилось заново
# создавать экземпляр Employee в каждом тестовом методе. Запустите
# свой тестовый сценарий и убедитесь в том, что оба теста прошли успешно.

class Employee:
    """Простая модель работника"""

    def __init__(self, last_name, first_name, annual_salary):
        """Инициализация имени, фамилии, ежегодного оклада."""
        self.last_name = last_name
        self.first_name = first_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Увеличивает ежегодный оклад на заданное значение."""
        self.annual_salary += raise_amount
        print(f"Оклад {self.first_name} {self.last_name} увеличен до {self.annual_salary}.")
