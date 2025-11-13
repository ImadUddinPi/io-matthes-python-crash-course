# # 9-1
# class Restaurant:
#     def __init__(self, res_name, cuisine_type):
#         self.restaurant_name = res_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):
#         print(f"The {self.restaurant_name} restaurant serves {self.cuisine_type} food")

#     def open_restaurant(self):
#         print(f"The {self.restaurant_name} is open now")


# # r1 = Restaurant("four seasons", "spicy")
# # r1.describe_restaurant()
# # r1.open_restaurant()

# # 9-2
# r1 = Restaurant("four seasons", "spicy")
# r2 = Restaurant("shah g", "expensive")
# r3 = Restaurant("quetta", "tasty")

# r2.describe_restaurant()


# 9-3
class User:
    def __init__(self, fn, ln, **kwargs):
        self.f_name = fn
        self.l_name = ln
        self.args = {}
        for key, value in kwargs.items():
            self.args[key] = value

    def describe_user(self):
        print(f"{self.f_name} {self.l_name}'s info:")
        for key, value in self.args.items():
            print(f"{key}: {value}")

    def greet_user(self):
        print(f"hello, {self.f_name}")


u1 = User("john", "doe", age=22, city="NY", country="US")
u1.describe_user()

u2 = User("hamza", "sheeno", age=100, city="tappi", country="kohat")
u2.describe_user()
u2.greet_user()
