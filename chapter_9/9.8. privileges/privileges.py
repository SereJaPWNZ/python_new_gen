# 9.8. Привилегии: напишите класс Privileges. Класс должен содержать всего один
# атрибут privileges со списком строк из упражнения 9.7. Переместите метод show_privileges()
# в этот класс. Создайте экземпляр Privileges как атрибут класса Admin. Создайте новый
# экземпляр Admin и используйте свой метод для вывода списка привилегий.

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


class Privileges:
    """Класс, который хранит список привилегий администратора."""

    def __init__(self, privileges=None):
        """Инициализация атрибута privileges."""
        if privileges is None:
            privileges = ["разрешено добавлять сообщения",
                          "разрешено удалять пользователей",
                          "разрешено банить пользователей"]
        self.privileges = privileges

    def show_privileges(self):
        """Выводит набор привилегий администратора."""
        counter = 1
        for privilege in self.privileges:
            print(counter, "-", privilege)
            counter += 1


class Admin(User):
    """Предоставляет аспекты пользователя, с расширенными правами."""

    def __init__(self, first_name, last_name, login_attempts=0, university=None, bpl=None):
        """Инициализация атрибутов класса родителя."""
        super().__init__(first_name,
                         last_name,
                         login_attempts,
                         university,
                         bpl)
        # Создание экземпляра Privileges как атрибута класса Admin
        self.privileges = Privileges()


admin = Admin("Andrey",
              "Petrov",
              0,
              "vstu",
              "volgograd")
# Использование метода show_privileges() из класса Privileges
admin.privileges.show_privileges()
