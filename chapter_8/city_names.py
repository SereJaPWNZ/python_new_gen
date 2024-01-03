# 8.6. Названия городов: напишите функцию city_country(), которая получает название
# города и страну. Функция должна возвращать строку в формате "Santiago, Chile". Вызовите
# свою функцию по крайней мере для трех пар «город — страна» и выведите возвращенное
# значение.

def city_country(city=None, country=None):
    """Выводит отформатированную строку с названием города и страны"""
    if city and country and country != ' ':
        format_text = f'\n{city.title()}, {country.title()}'
    elif city:
        format_text = f'\n{city.title()}'
    else:
        format_text = f'\nПоля не заполнены'
    return format_text


while True:
    print("\nПожалуйста внесите ваше имя:"
          "\nДля выхода из программы введите \"q\" или оставьте пустое значение.")
    city = input('Название города: ')
    if city.lower() == 'q' or city == '':
        break
    country = input('Название страны: ')
    if country.lower() == 'q' or city == '':
        break
    print(city_country(city, country))
