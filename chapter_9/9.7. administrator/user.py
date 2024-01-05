# 9.7. Администратор: администратор — особая разновидность пользователя. Напишите
# класс с именем Admin, наследующий от класса User из упражнения 9.3 или упражнения 9.5
# (с. 180). Добавьте атрибут privileges для хранения списка строк вида "разрешено добавлять
# сообщения", "разрешено удалять пользователей", "разрешено банить пользователей" и т. д.
# Напишите метод show_privileges() для вывода набора привилегий администратора. Создайте
# экземпляр Admin и вызовите свой метод.

class User:
    """Простая модель пользователя"""

    def __init__(self, first_name, last_name, login_attempts=0, university=None, bpl=None):
        """Инициализация имени и фамилии пользователя"""
        self.first_name = first_name
        self.last_name = last_name
        self.university = university
        self.login_attempts = login_attempts
        self.bpl = bpl

    def describe_user(self):
        """Выводит сводку с информацией о пользователе"""
        description = (f'\nИмя: {self.first_name.title()}'
                       f'\nФамилия: {self.last_name.title()}')
        if self.university is not None:
            description += f'\nВУЗ: {self.university.upper()}'
        if self.bpl is not None:
            description += f'\nМесто рождения: {self.bpl.title()}'
        return description

    def greet_user(self):
        """Выводит персональное приветствие"""
        greeting = f"Здравствуйте, {self.last_name} {self.first_name}!"
        return greeting

    def increment_login_attempts(self):
        """Увеличивает значение login_attempts на 1."""
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        """Обнуляет значение login_attempts."""
        self.login_attempts = 0
        return self.login_attempts


person1 = User("Andrey", "Petrov", 0, "vstu", "volgograd")
