# 9.12. Множественные модули: сохраните класс User в одном модуле, а классы Privileges
# и Admin в другом модуле. В отдельном файле создайте экземпляр Admin и вызовите метод
# show_privileges(), чтобы показать, что все работает правильно.

from user import User
from privileges import Privileges


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
