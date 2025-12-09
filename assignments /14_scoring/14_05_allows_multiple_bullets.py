# I will allow multiple correct answers for multiple bullets
def allow_multiple_bullets(questions):
    for question in questions:
        if question['type'] == 'multiple_bullets':
            question['allows_multiple_correct'] = True
        else:
            question['allows_multiple_correct'] = False
    return questions