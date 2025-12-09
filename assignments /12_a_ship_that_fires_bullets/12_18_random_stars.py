# I will make a random star
import random
def draw_random_star():
    size = random.randint(3, 7)
    for i in range(size):
        print("* " * size)
# Call the draw_random_star function to test it
draw_random_star()