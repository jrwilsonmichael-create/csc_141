# I will add a fleet direction
fleet = [
    {'name': 'Aragnith', 'type': 'Destroyer', 'speed':
        30, 'direction': 'North'},
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