# I will add powerips
def add_powerups(player, powerups):
    for powerup in powerups:
        if powerup == "speed":
            player["speed"] += 10
        elif powerup == "strength":
            player["strength"] += 5
        elif powerup == "health":
            player["health"] += 20
    return player
# Example usage
player = {"speed": 50, "strength": 30, "health": 100}
powerups = ["speed", "health", "strength"]
player = add_powerups(player, powerups)
print("Updated player stats:", player)