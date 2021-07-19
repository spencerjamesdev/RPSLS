from player import Player
import random


class Computer(Player):

    def __init__(self):
        self.computer_score = 0
        super().__init__()

    #this method picks a random choice for the AI and returns it
    def computer_move(self):
        computer_choice = random.choice(self.gesture_list)
        return computer_choice

