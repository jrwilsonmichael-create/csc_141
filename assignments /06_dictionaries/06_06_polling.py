# I will do a polling program
responses = {}
polling_active = True

while polling_active:
    name = input("What do you eat for breakfast? ")
    response = input("What is your favorite breakfast food? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to eat {response} for breakfast.")