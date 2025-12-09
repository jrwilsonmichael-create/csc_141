# I will make a scoring system
def calculate_score(enemies_destroyed, bonus):
    score = enemies_destroyed * 100 + bonus
    print(f"Your total score is: {score}")
    return score
# Call the calculate_score function to test it
calculate_score(15, 500)