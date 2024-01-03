# 8.5. Города: напишите функцию describe_city(), которая получает названия города
# и страны. Функция должна выводить простое сообщение (например, «Reykjavik is in
# Iceland»). Задайте параметру страны значение по умолчанию. Вызовите свою функцию
# для трех разных городов, по крайней мере один из которых не находится в стране по
# умолчанию.


def describe_city(city, country='Russia'):
    """Выводит сообщение о городе и стране"""
    message = f'{city.title()} is in {country.title()}'
    return message


print(describe_city('Volgograd'))
print(describe_city('New-York', country='USA'))
