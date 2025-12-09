# I will do a lotter analysis
from _09_14_lottery.py import Lottery
class LotteryAnalysis:
    def __init__(self, lottery):
        self.lottery = lottery

    def simulate_draws(self, num_draws):
        results = {}
        for _ in range(num_draws):
            winner = self.lottery.draw_winner()
            if winner in results:
                results[winner] += 1
            else:
                results[winner] = 1
        return results
