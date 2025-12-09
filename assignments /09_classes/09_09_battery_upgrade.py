# I will create a BatteryUpgrade class
class BatteryUpgrade:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def upgrade_battery(self):
        """Upgrade the battery size to 85 if it is less than 85."""
        if self.battery_size < 85:
            self.battery_size = 85

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")