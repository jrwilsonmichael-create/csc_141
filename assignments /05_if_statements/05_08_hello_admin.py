# I will be greeting the admin user
users = ['Mike']
for user in users:
    if user == 'admin':
        print("Good morning admin, would you ike to see a status report?")
    else:
            print(f"Hello {user}, thank you for logging in again.")