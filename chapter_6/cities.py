# 6.11. Города: создайте словарь с именем cities. Используйте названия трех городов
# в качестве ключей словаря. Создайте словарь с информацией о каждом городе; включите в него
# страну, в которой расположен город, примерную численность населения и один примечательный факт,
# относящийся к этому городу. Ключи словаря каждого города должны называться country,
# population и fact. Выведите название каждого города и всю сохраненную
# информацию о нем.

cities = {
    "Moscow": {
        "country": "Russia",
        "population": "12.5 million",
        "fact": "Moscow is home to the largest number of billionaires in the world."
    },
    "New York": {
        "country": "United States",
        "population": "8.3 million",
        "fact": "New York City is the most linguistically diverse city in the world, with over 800 languages spoken."
    },
    "Tokyo": {
        "country": "Japan",
        "population": "9.3 million",
        "fact": "Tokyo is the most populous metropolitan area in the world, with over 37 million people."
    }
}

for city, fact in cities.items():
    print(f'Название города: {city}\nВ какой стране находится: {fact["country"]}\nПопуляция: {fact["population"]}\n'
          f'Интересный факт: {fact["fact"]}')
    print()
