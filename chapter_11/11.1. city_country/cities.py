from city_functions import get_formatted_city

print(f"Введите 'q' для выхода")

while True:
    city = input("Введите название города:\n")
    if city == 'q' or city == '':
        break
    country = input("Введите название страны:\n")
    if country == 'q' or country == '':
        break

    formatted_city = get_formatted_city(city, country)
    print(formatted_city)
