# 9.11. Импортирование класса Admin: начните с версии класса из упражнения 9.8 (с. 186).
# Сохраните классы User, Privileges и Admin в одном модуле. Создайте отдельный файл,
# создайте экземпляр Admin и вызовите метод show_privileges(), чтобы показать, что все
# работает правильно.

from privileges import Admin


admin = Admin("Andrey",
              "Petrov",
              0,
              "vstu",
              "volgograd")

# Использование метода show_privileges() из класса Privileges
admin.privileges.show_privileges()
