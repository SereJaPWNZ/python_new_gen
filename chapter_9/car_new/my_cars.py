from car import Car
from electric_car import ElectricCar

my_beetle = Car("volkswagen", "beetle", 1975)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("tesla", "x", 2015)
print(my_tesla.get_descriptive_name())
