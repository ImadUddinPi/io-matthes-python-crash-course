# # 9-6 ICE-CREAM STAND
# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         self.name = name
#         self.cuisine_type = cuisine_type
#         self.people_served = 0

#     def describe_restaurant(self):
#         print(f"The {self.name} serves {self.cuisine_type} food.")


# class IceCreamStand(Restaurant):
#     def __init__(self, name, cuisine_type, *flavors):
#         super().__init__(name, cuisine_type)
#         self.flavors = []
#         for flavor in flavors:
#             self.flavors.append(flavor)

#     def available_flavors(self):
#         print(f"available flavors are:")
#         for flavor in self.flavors:
#             print(f"-{flavor}")


# s1 = IceCreamStand("dunkin", "sweet", "vanilla", "choco", "strawB")
# s1.available_flavors()


# # 9-7 ADMIN
# class User:
#     def __init__(self, fname, lname, **kwargs):
#         self.fname = fname
#         self.lname = lname
#         self.kwargs = {}
#         for key, value in kwargs.items():
#             self.kwargs[key] = value


# class Admin(User):
#     def __init__(self, fname, lname, **kwargs):
#         super().__init__(fname, lname, **kwargs)
#         self.privileges = ["can add post", "can delete post", "can ban user"]

#     def describe_user(self):
#         print(f"Info of {self.fname} {self.lname}:")
#         for key, value in self.kwargs.items():
#             print(key, value)

#     def show_privileges(self):
#         print(f"Privileges of User:")
#         for val in self.privileges:
#             print(f"-{val}")


# a1 = Admin("joe", "cleveland", age=25, city="quahog")
# a1.show_privileges()


# # 9-8 PRIVILEGES
# class User:
#     def __init__(self, fname, lname, **kwargs):
#         self.fname = fname
#         self.lname = lname
#         self.kwargs = {}
#         for key, value in kwargs.items():
#             self.kwargs[key] = value


# class Admin(User):
#     def __init__(self, fname, lname, **kwargs):
#         super().__init__(fname, lname, **kwargs)
#         self.privileges = Privileges()

#     def describe_user(self):
#         print(f"Info of {self.fname} {self.lname}:")
#         for key, value in self.kwargs.items():
#             print(key, value)


# class Privileges:
#     def __init__(self):
#         self.privileges = ["can add post", "can delete post", "can ban user"]

#     def show_privileges(self):
#         print(f"Privileges of User:")
#         for val in self.privileges:
#             print(f"-{val}")


# a1 = Admin("peter", "griffin", age=99)
# a1.privileges.show_privileges()


# 9-9 BATTERY UPGRADE
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

    def upgrade_battery(self):
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """init attrs of parent"""
        super().__init__(make, model, year)
        self.battery = Battery()


c1 = ElectricCar("dodge", "angle", 2077)
c1.battery.get_range()
c1.battery.upgrade_battery()
c1.battery.get_range()
