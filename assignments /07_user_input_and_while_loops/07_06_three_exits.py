# I will make 3 exits 
while True:
    user_input = input("Type 'exit1', 'exit2', or 'exit3' to exit the loop: ")
    
    if user_input == 'exit1':
        print("Exiting through exit 1!")
        break
    elif user_input == 'exit2':
        print("Exiting through exit 2!")
        break
    elif user_input == 'exit3':
        print("Exiting through exit 3!")
        break
    else:
        print("Invalid input, please try again.")