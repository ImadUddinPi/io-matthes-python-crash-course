# class Dog:
#     def __init__(self, name, age):
#         """initialize with init values"""
#         self.name = name
#         self.age = age

#     def sit(self):
#         """simulate a dog sitting"""
#         return f"{self.name} is now sitting!"

#     def roll_over(self):
#         """simulate a dog rolling over"""
#         return f"{self.name} is rolling now!"


# d1 = Dog("brian", 5)

# # print(d1.__dict__)
# print(Dog.__dict__.keys())

# func = d1.sit
# print(func)
# print(Dog.sit(d1))

# Working with Classes and Instances


class Car:
    def __init__(self, make, model, year):
        """initialize attrs to describe a car"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """return neatly formatted descriptive name"""
        print(f"{self.year} {self.make}, {self.model}")


c1 = Car("Aston Martin", "DB9", 1999)
c1.get_descriptive_name()
