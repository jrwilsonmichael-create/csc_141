# I will be doing a target pratice
def target_practice(targets, shots):
    hits = 0
    for shot in shots:
        if shot in targets:
            hits += 1
    return hits
# Example usage:
targets = [(1, 2), (3, 4), (5, 6)]
shots = [(1, 2), (7, 8), (3, 4), (9, 10)]
print(target_practice(targets, shots))  # Output: 2