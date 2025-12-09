# I will do a lottery class
import random
class Lottery:
    def __init__(self, participants):
        self.participants = participants

    def draw_winner(self):
        return random.choice(self.participants)