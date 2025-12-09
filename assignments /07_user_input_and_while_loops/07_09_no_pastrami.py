# I will add pastrami to the list
sandwich_orders = ["Ham Sandwich", "Pastrami Sandwich", "Honey Turkey Sandwich", "Pastrami Sandwich", "Turkey Ham Sandwich", "Pastrami Sandwich"]
finished_sandwiches = []
print("The deli has run out of pastrami.")
while "Pastrami Sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami Sandwich")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)