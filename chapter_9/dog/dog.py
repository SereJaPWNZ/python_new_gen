class Dog:
    """Простая модель собаки"""

    def __init__(self, name, age):
        """Инициализирует атрибуты name, age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name.title()} rolled over")


my_dog = Dog('willie', 15)
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")
my_dog.sit()
my_dog.roll_over()
