# # DEFAULT VALUES
# def describe_pet(pet_name, animal_type="dog"):
#     """display pet's information"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")


# # ways of calling paramed funcs
# describe_pet(pet_name="Willie")
# describe_pet("Jack")
# describe_pet(pet_name="nate", animal_type="cat")
# describe_pet(animal_type="fish", pet_name="nate")


# # RETURNING A SIMPLE VALUE
# def get_formatted_name(f_name, l_name):
#     """returns full name, formatted!"""
#     full_name = f"{f_name} {l_name}"
#     return full_name.title()


# musician = get_formatted_name("jimi", "hendrix")
# print(musician)


# def get_formatted_name(f_name, l_name):
#     """return a full name, neatly formatted."""
#     full_name = f"{f_name} {l_name}"
#     return full_name.title()


# while True:
#     print("\nPllease tell me your name:")
#     f_name = input(f"First Name: ")
#     l_name = input(f"Last Name: ")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\n Hello, {formatted_name}")


# def get_formatted_name(f_name, l_name, m_name=""):
#     """return a full name, neatly formatted."""
#     full_name = f"{f_name} {l_name}"
#     return full_name.title()


# while True:
#     print("\nPllease tell me your name:")
#     print("To exit press q")
#     f_name = input(f"First Name: ")
#     if f_name == "q":
#         break
#     l_name = input(f"Last Name: ")
#     if l_name == "q":
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\n Hello, {formatted_name}")


# # PASSING A LIST
# def greet_users(names):
#     """print greeting to each user in list"""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)


# names = ["abc", "def", "ghi"]
# greet_users(names)

# # MODIFYING A LIST IN A FUNCTION
# unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
# completed_models = []

# # # simulate printing each design, until none left
# # while unprinted_designs:
# #     current_design = unprinted_designs.pop()
# #     print(f"Printing model: {current_design}")
# #     completed_models.append(current_design)

# # print("\nThe following models have been printed:")
# # for completed_model in completed_models:
# #     print(completed_model)


# def print_models(unprinted_designs, completed_models):
#     """Simulate printing the unprinted, until none left.
#     Move each design to completed once done printing it"""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)


# def rendered_models(completed_models):
#     print(f"Models printed are:")
#     for model in completed_models:
#         print(model)


# print_models(unprinted_designs[:], completed_models)
# print(f"Assets Array: {unprinted_designs}")
# rendered_models(completed_models)


# # PASSING AN ARBITRARY NUMBER OF ARGUMENTS
# def make_pizza(*toppings):
#     """print list of toppings requested"""
#     print("\nMaking a pizza with following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza("extra-cheese")
# make_pizza("pepperoni", "cheese", "jalapeno")


# # MIXING POSITIONAL AND ARBITRARY ARGUMENTS
# def make_pizza(size, *toppings):
#     """summarize pizza being made"""
#     print(f"\nMaking a {size}-inch pizza with ingredients:")
#     for top in toppings:
#         print(f"-{top}")


# make_pizza(16, "pepperoni")
# make_pizza(16, "shrooms", "jane", "ganja")


# USING ARBITRARY KEYWORD ARGUMENTS
def build_profile(first, last, **user_info):
    """build a dict containing everything we
    know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics"
)
print(user_profile)
