# I will create a login attempts class
class LoginAttempts:
    def __init__(self):
        self.attempts = 0

    def increment_attempts(self):
        """Increment the number of login attempts by 1."""
        self.attempts += 1

    def reset_attempts(self):
        """Reset the number of login attempts to 0."""
        self.attempts = 0
# Example usage:
login = LoginAttempts()
login.increment_attempts()
print(f"Login attempts: {login.attempts}")  # Output: Login attempts: 1
login.increment_attempts()