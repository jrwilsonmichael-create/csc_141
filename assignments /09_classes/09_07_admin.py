# I will make an amin function
def make_admin(username, privileges=None):
    """Return a dictionary representing an admin user."""
    admin_dict = {
        'username': username.title()
    }
    if privileges is not None:
        admin_dict['privileges'] = privileges
    return admin_dict
# Example usage:
print(make_admin("aragnith", ["can add post", "can delete post", "can ban user"]))