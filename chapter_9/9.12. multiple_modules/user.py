# 9.12. Множественные модули: сохраните класс User в одном модуле, а классы Privileges
# и Admin в другом модуле. В отдельном файле создайте экземпляр Admin и вызовите метод
# show_privileges(), чтобы показать, что все работает правильно.

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
