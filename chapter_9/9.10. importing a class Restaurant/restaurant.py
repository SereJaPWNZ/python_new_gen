# 9.10. Импортирование класса Restaurant: возьмите последнюю версию класса Restaurant
# и сохраните ее в модуле. Создайте отдельный файл, импортирующий класс Restaurant.
# Создайте экземпляр Restaurant и вызовите один из методов Restaurant, чтобы показать,
# что команда import работает правильно.

from modul_restaurant import Restaurant

Restaurant = Restaurant("viuga", "russian")
Restaurant.open_restaurant(1915)
