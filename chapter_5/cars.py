cars = ['audi', 'bmw', 'subaru', 'toyota']

# проверка по содержанию в переменной car значения bmw
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
