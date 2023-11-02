# string concatenation
# suppose we want to creat a string that says "subscribe to ____"
# youtuber = "TheSoulDude" # some string variable

# # a few ways to do this
# print("subscibe to " + youtuber)
# print("subscibe to {}".format(youtuber))
# print(f"subscibe to {youtuber}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)