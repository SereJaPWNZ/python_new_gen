from car import Car

my_new_car = Car("audi", "m5", 2010)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(10)
my_new_car.read_odometer()
