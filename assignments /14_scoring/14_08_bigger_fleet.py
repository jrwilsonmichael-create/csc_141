# I will a a bigger fleet
fleet = [
    {'name': 'Aragnith', 'type': 'Destroyer', 'speed': 30},
    {'name': 'Tereth', 'type': 'Cruiser', 'speed': 25},
    {'name': 'Queen bee', 'type': 'Battleship', 'speed': 20},
    {'name': 'Dreadnought', 'type': 'Carrier', 'speed': 15},
    {'name': 'Valkyrie', 'type': 'Frigate', 'speed': 35},
    {'name': 'Leviathan', 'type': 'Battleship', 'speed': 18},
    {'name': 'Phantom', 'type': 'Destroyer', 'speed': 32},
    {'name': 'Titan', 'type': 'Cruiser', 'speed': 28},
    {'name': 'Spectre', 'type': 'Frigate', 'speed': 33},
    {'name': 'Colossus', 'type': 'Carrier', 'speed': 12}
]
def score_fleet(fleet):
    score = 0
    for ship in fleet:
        if ship['type'] == 'Destroyer':
            score += 150 + ship['speed'] * 3
        elif ship['type'] == 'Cruiser':
            score += 100 + ship['speed'] * 2
        elif ship['type'] == 'Battleship':
            score += 200 + ship['speed'] * 1.5
        elif ship['type'] == 'Carrier':
            score += 250 + ship['speed'] * 1
        elif ship['type'] == 'Frigate':
            score += 80 + ship['speed'] * 4
    return score