class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self, relaxed=False, smart=False, goofy=False, hyper=False):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and lives in {self.city}.")
        print("Personality traits:")
        if relaxed:
            print("- Relaxed")
        if smart:
            print("- Smart")
        if goofy:
            print("- Goofy")
        if hyper:
            print("- Hyper")
        self.greet_user()

    def greet_user(self):
        print(f"Greetings, {self.first_name} {self.last_name}!")

# Example usage
user1 = User('Tahjay', 'Green', 18, 'Philadelphia')
user1.describe_user(relaxed=True, smart=True, goofy=True, hyper=False)