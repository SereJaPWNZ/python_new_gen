import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Тесты для класса employee."""

    def setUp(self):
        """Создание экземпляра Employee для использования во всех тестовых методах."""
        self.my_employee = Employee("Sergey", "Shevtsov", 100000)

    def test_give_default_raise(self):
        """Сверяет стандартное значение повышения зарплаты."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.annual_salary, 105000)

    def test_give_custom_raise(self):
        """Сверяет не стандартное значение повышения зарплаты."""
        self.my_employee.give_raise(15000)
        self.assertEqual(self.my_employee.annual_salary, 115000)


if __name__ == "__main__":
    unittest.main()
