from car import Car
#from games_python.car import Car

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2022)

# Accessing attributes of the instance
print(my_car.make)  # Output: Toyota
print(my_car.model)  # Output: Camry
print(my_car.year)  # Output: 2022

# Calling methods of the instance
my_car.start()  # Output: The car has been started.
my_car.drive(10)  # Output: The Toyota Camry is driving 10 miles.
my_car.stop()  # Output: The car has been stopped.
