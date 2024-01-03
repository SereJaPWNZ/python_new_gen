class User:
    """Простая модель пользователя"""

    def __init__(self, first_name, last_name, university=None, bpl=None):
        """Инициализация имени и фамилии пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.university = university
        self.bpl = bpl

    def describe_user(self):
        """Выводит сводку с информацией о пользователе"""
        description = (f'\nИмя: {self.first_name.title()}'
                       f'\nФамилия: {self.last_name.title()}')
        if self.university:
            description += f'\nВУЗ: {self.university.upper()}'
        if self.bpl:
            description += f'\nМесто рождения: {self.bpl.title()}'
            return description

    def greet_user(self):
        """Выводит персональное приветствие"""
        greeting = f"Здравствуйте, {self.last_name} {self.first_name}!"
        return greeting


person1 = User("Andrey", "Petrov", "vstu", "volgograd")
print(person1.describe_user())
print(person1.greet_user())

person2 = User("Ivan", "Andreev")
print(person2.describe_user())
print(person2.greet_user())
