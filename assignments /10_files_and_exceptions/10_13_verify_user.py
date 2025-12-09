# I will make a fuction that recognizes the user
def greet_user():
    """Greet the user by name."""
    try:
        with open('username.txt', 'r') as file:
            username = file.read()
    except FileNotFoundError:
        username = input("What is your name? ")
        with open('username.txt', 'w') as file:
            file.write(username)
    print(f"Welcome back, {username}!")
greet_user()