# I will do similar sentences function
def similar_sentences(sentence1, sentence2):
    """Check if two sentences are similar by comparing their words."""
    words1 = set(sentence1.lower().split())
    words2 = set(sentence2.lower().split())
    common_words = words1.intersection(words2)
    similarity_ratio = len(common_words) / max(len(words1), len(words2))
    return similarity_ratio >= 0.5
# Example usage:
print(similar_sentences("I have a imaginary pet dragon", "My pet dragon is named Aragnith"))
print(similar_sentences("The sky is blue", "The ocean is blue"))