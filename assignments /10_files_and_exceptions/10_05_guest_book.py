# I will make a guest book function
def add_guest(guest_book, name):
    """Add a guest's name to the guest book list."""
    guest_book.append(name.title())
# Example usage:
guest_book = []
add_guest(guest_book, "aragnith rusty")
add_guest(guest_book, "luna lovegood")
print(guest_book)  # Output: ['Aragnith Rusty', 'Luna Lovegood']