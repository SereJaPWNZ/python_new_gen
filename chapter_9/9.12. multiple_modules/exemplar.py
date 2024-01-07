# 9.12. Множественные модули: сохраните класс User в одном модуле, а классы Privileges
# и Admin в другом модуле. В отдельном файле создайте экземпляр Admin и вызовите метод
# show_privileges(), чтобы показать, что все работает правильно.

from admin import Admin

admin = Admin("Sergey", "Shevtsov", "3434", "VolgSTU", "ffdfd")
admin.privileges.show_privileges()

