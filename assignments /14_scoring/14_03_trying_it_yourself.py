# I will be trying it on myself
def calculate_score(true_labels, predicted_labels): 
    """
    Calculate the accuracy score given true labels and predicted labels.

    Parameters:
    true_labels (list): A list of true labels.
    predicted_labels (list): A list of predicted labels.

    Returns:
    float: The accuracy score as a percentage.
    """
    if len(true_labels) != len(predicted_labels):
        raise ValueError("The length of true_labels and predicted_labels must be the same.")

    correct_predictions = sum(t == p for t, p in zip(true_labels, predicted_labels))
    total_predictions = len(true_labels)

    accuracy = (correct_predictions / total_predictions) * 100
    return accuracy
# Example usage
true_labels = [1, 0, 1, 1, 0, 1, 0]
predicted_labels = [1, 0, 0, 1, 0, 1, 1]
score = calculate_score(true_labels, predicted_labels)  
print(f"Accuracy score: {score}%")