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
