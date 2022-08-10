# name = input("Name: ")
# count = 0
# for letter in name:
#     if letter.lower() in "aeiou":
#         count += 1
# print("Out of {} letters, {} has {} vowels.".format(len(name), name, count))

name = input("Name: ")
vowels = [char for char in name if char.lower() in "aeiou"]
print("Out of {} letters, {} has {} vowels, and there are {}.".format(len(name), name, len(vowels), vowels))

