# I will be archiving messages
def archive_message(message, archived_messages):
    """Archive a message by adding it to the archived_messages list.

    Args:
        message (str): The message to be archived.
        archived_messages (list): The list where archived messages are stored.

    Returns:
        None: The function modifies the archived_messages list in place.
    """
    archived_messages.append(message)
# Example usage:
archived = []
archive_message("Hello, World!", archived)
print(archived)  # Output: ['Hello, World!']