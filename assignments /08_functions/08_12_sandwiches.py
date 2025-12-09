# I will be making sandwiches
def make_sandwich(*ingredients):
    """Make a sandwich with the given ingredients.

    Args:
        *ingredients: Variable length argument list of sandwich ingredients.

    Returns:
        A string describing the sandwich made with the given ingredients.
    """
    sandwich = "Sandwich with " + ", ".join(ingredients)
    return sandwich
# Example usage:
print(make_sandwich("ham", "cheese", "lettuce", "tomato", "pickles"))
print(make_sandwich("turkey", "ham", "mayo", "Extra pickles"))
print(make_sandwich("peanut butter", "jelly"))