# Любимые места: создайте словарь с именем favorite_places. Придумайте названия
# трех мест, которые станут ключами словаря, и сохраните для каждого человека от одного
# до трех любимых мест. Чтобы задача стала более интересной, опросите нескольких друзей
# и соберите реальные данные для своей программы. Переберите данные в словаре, выведите
# имя каждого человека и его любимые места.

favorite_places = {
    "Анна": ["Париж", "Пляж Коктебель", "Горы Алтая"],
    "Иван": ["Лондон", "Озеро Байкал", "Нью-Йорк"],
    "Мария": ["Барселона", "Венеция", "Национальный парк Йосемити"]
}

for name, places in favorite_places.items():
    print(f'Любимые места {name}:')
    for i in range(len(places)):
        print(f'{i + 1}) {places[i]}')
    print()
