from player import Player


class Human(Player):

    def __init__(self):
        self.human_score = 0
        super().__init__()

    #this method has the user pick 1-5 to select a gesture. returns that gesture and returns false if not 1-5
    def human_move(self):
        user_input = input("Make your move! \nRock: '1' \nPaper: '2' \nScissors: '3' \nLizard: '4' \nSpock: '5' \nPlease pick a number 1-5: ")
        if user_input == '1':
            user_input = "Rock"
        if user_input == '2':
            user_input = "Paper"
        if user_input == '3':
            user_input = "Scissors"
        if user_input == '4':
            user_input = "Lizard"
        if user_input == '5':
            user_input = "Spock"
        return user_input

