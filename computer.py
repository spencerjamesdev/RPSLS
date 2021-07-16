from player import Player
import random


class Computer(Player):

    def __init__(self):
        self.computer_score = 0
        super().__init__()


    def computer_move(self):
        computer_choice = random.choice(self.gesture_list)
        print(computer_choice)

sup = Computer()
sup.computer_move()