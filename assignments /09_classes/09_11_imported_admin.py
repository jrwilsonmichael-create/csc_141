# I will import the admin module
from assignments._09_classes._09_07_admin import make_admin
# Create an admin user using the imported function
admin_user = make_admin("aragnith", ["can add post", "can delete post", "can ban user"])
# Display the admin user's details
print(admin_user)