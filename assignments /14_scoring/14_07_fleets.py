# I will add a fleet
def add_fleet(fleets, new_fleet):
    """
    Adds a new fleet to the list of fleets.

    Parameters:
    fleets (list): A list of existing fleets.
    new_fleet (dict): A dictionary representing the new fleet to be added.

    Returns:
    list: Updated list of fleets including the new fleet.
    """
    fleets.append(new_fleet)
    return fleets