# I will be checking usernames
current_users = ['Mikey', 'Mike A', 'Jordan']
new_users = ['Mike','mike a', 'jordan']
for new_users in new_users:
    if new_users.lower() in [user.lower() for user in current_users]:
        print(f"Sorry {new_users}, that username is taken. Please enter a new username.")