# I will be adding a difficulty score 
def add_difficulty_score(questions):
    for question in questions:
        if question['type'] == 'multiple_choice':
            question['difficulty_score'] = 1
        elif question['type'] == 'true_false':
            question['difficulty_score'] = 0.5
        elif question['type'] == 'short_answer':
            question['difficulty_score'] = 2
        else:
            question['difficulty_score'] = 1.5  # Default score for unknown types
    return questions