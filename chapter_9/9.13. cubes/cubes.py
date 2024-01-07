# 9.13. Кубики: создайте класс Die с одним атрибутом sides, который
# имеет значение по умолчанию 6. Напишите метод roll_die() для вывода
# случайного числа от 1 до количества граней на кубике. Создайте
# экземпляр, представляющий 6-гранный кубик, и смоделируйте 10 бросков.
# Создайте экземпляры, представляющие 10- и 20-гранный кубик.
# Смоделируйте 10 бросков каждого кубика.
from random import randint


class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides=6):
        """Initialize attributes of the die."""
        self.sides = sides

    def roll_die(self):
        """Return a random value between 1 and number of sides."""
        random_number = randint(1, self.sides)
        return random_number
