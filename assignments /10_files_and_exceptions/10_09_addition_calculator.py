# I will make a addition calculator 
def addition_calculator():
    print("Welcome to the Addition Calculator!")
    print("Enter numbers to add them together. Type 'q' to quit.")

    total = 0

    while True:
        user_input = input("Enter a number (or 'q' to quit): ")

        if user_input.lower() == 'q':
            print(f"The final total is: {total}")
            print("Thank you for using the Addition Calculator. Goodbye!")
            break

        try:
            number = float(user_input)
            total += number
            print(f"Current total: {total}")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")
# Run the addition calculator
addition_calculator()
