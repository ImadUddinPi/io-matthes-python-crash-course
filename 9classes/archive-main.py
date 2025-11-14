class Dog:
    def __init__(self, name, age):
        """initialize with init values"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting"""
        return f"{self.name} is now sitting!"

    def roll_over(self):
        """simulate a dog rolling over"""
        return f"{self.name} is rolling now!"


d1 = Dog("brian", 5)

# print(d1.__dict__)
print(Dog.__dict__.keys())

func = d1.sit
print(func)
print(Dog.sit(d1))

Working with Classes and Instances


class Car:
    def __init__(self, make, model, year):
        """initialize attrs to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make}, {self.model}"
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


c1 = Car("Aston Martin", "DB9", 1999)
c1.get_descriptive_name()
c1.read_odometer()

# *Modifying Attribute Values
# # changing values:
# directly thorough an instance
# through a method
# increment through method

# directly through instance
# dot not to access attrs
c1.odometer_reading = 23
c1.read_odometer()

# via method
c1.update_odometer(20)
c1.read_odometer()

# increment via method
c1.increment_odometer(200)
c1.read_odometer()
