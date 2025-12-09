# I will make a list of sandwich orders
sandwich_orders = ["Peanutbutter and jelly Sandwich", "Ham Sandwich", "Turkey Sandwich", "Honey Turkey Sandwich"]
finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)