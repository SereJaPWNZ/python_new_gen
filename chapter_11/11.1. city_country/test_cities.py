import unittest
from city_functions import get_formatted_city


class CitiesTestCase(unittest.TestCase):
    """Тесты для city_function.py"""

    def test_city_country(self):
        """Правильно ли выводится 'Santiago, Chile' город со страной"""
        formatted_city = get_formatted_city("Santiago", "Chile")
        self.assertEqual(formatted_city, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()
