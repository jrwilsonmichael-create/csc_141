# I will be adding common words
def load_common_words(file_path):
    """Load common words from a file and return them as a set.

    Args:
        file_path (str): The path to the file containing common words. 
    Returns:
        set: A set of common words.
    """
    common_words = set()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                word = line.strip()
                if word:  # Ensure the line is not empty
                    common_words.add(word)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return common_words