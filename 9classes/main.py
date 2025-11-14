# # INHERITANCE
# class Car:
#     def __init__(self, make, model, year):
#         """initialize attrs to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0

#     def get_descriptive_name(self):
#         """return neatly formatted descriptive name"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         print(long_name.title())

#     def read_odometer(self):
#         """print car's mileage"""
#         print(f"The car has {self.odometer_reading} miles on it.")

#     def update_odometer(self, mileage):
#         """set odometer new val,
#         reject changes if it attempts to roll
#         the odometer back"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer")

#     def increment_odometer(self, miles):
#         """add given amount to odometer reading"""
#         self.odometer_reading += miles


# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         """init attrs of parent"""
#         super().__init__(make, model, year)


# my_leaf = ElectricCar("nissan", "leaf", 1950)
# my_leaf.get_descriptive_name()


# ATTRS AND METHODS FOR CHILD CLASS
# INHERITANCE
class Car:
    def __init__(self, make, model, year):
        """initialize attrs to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        print(long_name.title())

    def read_odometer(self):
        """print car's mileage"""
        print(f"The car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """set odometer new val,
        reject changes if it attempts to roll
        the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """add given amount to odometer reading"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"Filling gas now!")


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """evaluate mileage of car"""
        if self.battery_size == 40:
            range = 150
        if self.battery_size == 65:
            range = 225
        print(f"The car has a range of {range} on a full charge.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """init attrs of parent"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_leaf = ElectricCar("nissan", "leaf", 2026)
my_leaf.get_descriptive_name()
my_leaf.battery.describe_battery()
my_leaf.battery.battery_size = 65
my_leaf.battery.get_range()


# MODELING REAL-WORLD OBJECTS
