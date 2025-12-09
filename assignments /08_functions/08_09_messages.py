# I will add messages 
def show_messages(messages):
    """print each message in the list."""
    for messages in messages:
        print(messages)
        def send_messages(messages, sent_messages):
            """move each message to sent_messages after printing."""
            while messages:
                current_message = messages.pop()
                print(f"Sending message: {current_message}")
                sent_messages.append(current_message)