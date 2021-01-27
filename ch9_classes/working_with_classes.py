from car import Car, ElectricCar

# main program

# new_car = Car('audi', 'a4', 2019)
# new_car.odometer_reading = 48

# used_car = Car('subaru', 'outback', 2015)

# print(new_car.get_descriptive_name())
# used_car.update_odometer(23)
# used_car.increment_odometer(100)
# used_car.read_odometer()


""" Inherited electric car"""

tesla = ElectricCar('tesla', 'model s', 2019)
print(tesla.get_descriptive_name())
tesla.battery.get_range()
tesla.battery.upgrade_battery()
tesla.battery.get_range()
