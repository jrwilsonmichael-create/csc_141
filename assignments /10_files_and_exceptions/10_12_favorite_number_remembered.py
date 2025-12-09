# I will be remembering my favorite number
try:
    question = "What is your favorite number? "
    with open('favorite_number.txt', 'r') as file:
        favorite_number = file.read()
except FileNotFoundError:
    favorite_number = input(question)
    with open('favorite_number.txt', 'w') as file:
        file.write(favorite_number)
print(f"I know your favorite number! It's {favorite_number}.")