# I will be adding my favorite number
favorite_number = 1
with open('favorite_number.txt', 'w') as file:
    file.write(str(favorite_number))
# I will be reading my favorite number
with open('favorite_number.txt', 'r') as file:
    favorite_number = file.read()
print(f"My favorite number is: {favorite_number}")