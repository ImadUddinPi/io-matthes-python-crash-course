# # 8-6
# def city_country(city, country):
#     print(f'"{city}", "{country}"')


# city_country("Santiago", "Chile")
# city_country("Kingston", "Jamaica")
# city_country("NY", "US")


# # 8-7


# def make_album(artist, album, songs=None):
#     des_alb = {}
#     des_alb["artist"] = artist
#     des_alb["album"] = album
#     if songs:
#         des_alb["songs"] = songs
#     return des_alb


# print(make_album("the weeknd", "hurry up tomorrow"))
# print(make_album("Ye", "MBDTF", 16))


# # 8-8
# def make_album(artist, album, songs=None):
#     des_alb = {}
#     des_alb["artist"] = artist
#     des_alb["album"] = album
#     if songs:
#         des_alb["songs"] = songs
#     return des_alb


# while True:
#     print("Enter the artist album info:")
#     print("\nPress q to quit")
#     artist = input(f"Enter the artist name:")
#     if artist == "q":
#         break
#     album = input(f"Enter the album name:")
#     if album == "q":
#         break
#     print(make_album(artist, album))

# # 8-9
# msgs = ["get through", "soaring through", "swimming through", "floating through"]
# sent_msgs = []


# def send_msgs(msgs):
#     while msgs:
#         curr_msg = msgs.pop()
#         print(curr_msg)
#         sent_msgs.append(curr_msg)


# send_msgs(msgs)
# print(msgs)
# print(sent_msgs)

# # 8-10 && 8-11
# msgs = ["get through", "soaring through", "swimming through", "floating through"]
# sent_msgs = []


# def send_msgs(msgs):
#     while msgs:
#         curr_msg = msgs.pop()
#         print(curr_msg)
#         sent_msgs.append(curr_msg)


# send_msgs(msgs[:])
# print(msgs)
# print(sent_msgs)


# # 8-12
# def sandwich_asks(*flavors):
#     """sandwhich summary print"""
#     print(f"\nSandwich is made of: ")
#     for f in flavors:
#         print(f"-{f}")


# sandwich_asks("vanilla", "chocolate", "hazlenut")


# # 8-13
# def build_profile(first, last, **user_info):
#     """build a dict containing everything we
#     know about a user."""
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info


# me = build_profile("imad", "uddin", hobby="football", home="kohat", isSleepy=True)
# print(me)


# 8-14
def car_info(man, model, **car_info):
    car_info["manufacturer"] = man
    car_info["model"] = model
    return car_info


car1 = car_info("Ferrari", "F50", year=2025, WD=4)
print(car1)
