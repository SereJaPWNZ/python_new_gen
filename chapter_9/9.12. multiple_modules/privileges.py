# 9.12. Множественные модули: сохраните класс User в одном модуле, а классы Privileges
# и Admin в другом модуле. В отдельном файле создайте экземпляр Admin и вызовите метод
# show_privileges(), чтобы показать, что все работает правильно.

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
