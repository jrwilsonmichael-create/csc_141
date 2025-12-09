# I will create a Privileges class
class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Display the privileges."""
        if self.privileges:
            print("Privileges:")
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This user has no privileges.")