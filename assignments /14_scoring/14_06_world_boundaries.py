# I will add world boundaries
def add_world_boundaries(questions):
    for question in questions:
        if question['region'] == 'world':
            question['boundaries'] = {'north': 90, 'south': -90, 'east': 180, 'west': -180}
        elif question['region'] == 'north_america':
            question['boundaries'] = {'north': 83, 'south': 7, 'east': -52, 'west': -168}
        elif question['region'] == 'europe':
            question['boundaries'] = {'north': 71, 'south': 35, 'east': 40, 'west': -31}
        else:
            question['boundaries'] = None  # Default for unknown regions
    return questions