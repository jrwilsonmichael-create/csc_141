# I will make bigger aliens
def make_bigger_aliens(aliens, factor):
    bigger_aliens = []
    for alien in aliens:
        bigger_alien = {
            'color': alien['color'],
            'points': alien['points'] * factor,
            'speed': alien['speed'] * factor
        }
        bigger_aliens.append(bigger_alien)
    return bigger_aliens
# Example usage
original_aliens = [
    {'color': 'green', 'points': 5, 'speed': 1},
    {'color': 'yellow', 'points': 10, 'speed': 2},
    {'color': 'red', 'points': 15, 'speed': 3}
]
bigger_aliens = make_bigger_aliens(original_aliens, 2
)
for alien in bigger_aliens:
    print(alien)