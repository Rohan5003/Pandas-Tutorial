# numbers = []

# for i in range(8):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# unique_numbers = set(numbers)
# print("Unique numbers:", unique_numbers)

fav_lang = {}

for i in range(4):
    name = input(f"Enter name of friend {i+1}: ")
    language = input(f"Enter {name}'s favorite language: ")
    fav_lang[name] = language

print("\nFavorite languages dictionary:")
print(fav_lang)

