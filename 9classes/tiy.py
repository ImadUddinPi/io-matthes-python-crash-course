# # # 9-1
# # class Restaurant:
# #     def __init__(self, res_name, cuisine_type):
# #         self.restaurant_name = res_name
# #         self.cuisine_type = cuisine_type

# #     def describe_restaurant(self):
# #         print(f"The {self.restaurant_name} restaurant serves {self.cuisine_type} food")

# #     def open_restaurant(self):
# #         print(f"The {self.restaurant_name} is open now")


# # # r1 = Restaurant("four seasons", "spicy")
# # # r1.describe_restaurant()
# # # r1.open_restaurant()

# # # 9-2
# # r1 = Restaurant("four seasons", "spicy")
# # r2 = Restaurant("shah g", "expensive")
# # r3 = Restaurant("quetta", "tasty")

# # r2.describe_restaurant()


# # 9-3
# class User:
#     def __init__(self, fn, ln, **kwargs):
#         self.f_name = fn
#         self.l_name = ln
#         self.args = {}
#         for key, value in kwargs.items():
#             self.args[key] = value

#     def describe_user(self):
#         print(f"{self.f_name} {self.l_name}'s info:")
#         for key, value in self.args.items():
#             print(f"{key}: {value}")

#     def greet_user(self):
#         print(f"hello, {self.f_name}")


# u1 = User("john", "doe", age=22, city="NY", country="US")
# u1.describe_user()

# u2 = User("hamza", "shin-kuney", age=100, city="tappi", country="kohat")
# u2.describe_user()
# u2.greet_user()


# # 9-4 NUMBER SERVED
# class Restaurant:
#     def __init__(self, res_name, cuisine_type, number_served=0):
#         self.restaurant_name = res_name
#         self.cuisine_type = cuisine_type
#         self.number_served = number_served

#     def describe_restaurant(self):
#         print(
#             f"The {self.restaurant_name} restaurant served {self.cuisine_type} food for {self.number_served}"
#         )

#     def open_restaurant(self):
#         print(f"The {self.restaurant_name} is open now")

#     def set_number_served(self, num):
#         self.number_served = num

#     def increment_number_served(self, value):
#         self.number_served += value


# r1 = Restaurant("shah g", "spicy")
# r1.describe_restaurant()
# r1.number_served = 25
# r1.describe_restaurant()
# r1.set_number_served(250)
# r1.describe_restaurant()
# r1.increment_number_served(1000)
# r1.describe_restaurant()


# 9-5 LOGIN ATTEMPTS
class User:
    def __init__(self, fn, ln, login_attempts, **kwargs):
        self.f_name = fn
        self.l_name = ln
        self.login_attempts = login_attempts
        self.args = {}
        for key, value in kwargs.items():
            self.args[key] = value

    def describe_user(self):
        print(f"{self.f_name} {self.l_name}'s info:")
        for key, value in self.args.items():
            print(f"{key}: {value}")

    def greet_user(self):
        print(f"hello, {self.f_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


u1 = User("John", "Doe", 2, city="Kohat", job="Developer")
u1.describe_user()

print(u1.login_attempts)
u1.increment_login_attempts()
u1.increment_login_attempts()
u1.increment_login_attempts()
print(u1.login_attempts)
u1.reset_login_attempts()
print(u1.login_attempts)
