# I will be creating user profiles
def build_user_profile(first_name, last_name, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile
# Example usage:
user_profile = build_user_profile('Aragnith', 'Rusty', location='The Shire', field='Adventuring')
print(user_profile)
