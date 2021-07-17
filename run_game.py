from player import Player
from human import Human
from computer import Computer

class Run_game:
    

    def __init__(self):
        
        pass

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock! Best out of 3 wins.")
        print("Rules: \nRock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock")

    def single_or_two_player(self):
        pass

    def single_player_round(self):
        #instantiating human and computer objects
        h = Human()
        c = Computer()

        #checking if move is a tie
        if h.human_move == c.computer_move:
            print("It's a tie!")
            return "Tie"
        
        #if human picks rocks
        elif h.human_move == "Rock" and c.computer_move == "Paper":
            print("Paper covers Rock")
            return False
        elif h.human_move == "Rock" and c.computer_move == "Scissors":
            print("Rock crushes Scissors")
            return True
        elif h.human_move == "Rock" and c.computer_move == "Lizard":
            print("Rock crushes Lizard")
            return True
        elif h.human_move == "Rock" and c.computer_move == "Spock":    
            print("Spock vaporizes Rock")
            return False
        
        #if human picks paper
        elif h.human_move == "Paper" and c.computer_move == "Rock":
            print("Paper covers Rock")
            return True
        elif h.human_move == "Paper" and c.computer_move == "Scissors":
            print("Scissors cuts Paper")
            return False
        elif h.human_move == "Paper" and c.computer_move == "Lizard":
            print("Lizard eats Paper")
            return False
        elif h.human_move == "Paper" and c.computer_move == "Spock":
            print("Paper disproves Spock")
            return True

        #if human picks Scissors
        elif h.human_move == "Scissors" and c.computer_move == "Rock":
            print("Rock crushes Scissors")
            return False
        elif h.human_move == "Scissors" and c.computer_move == "Paper":
            print("Scissors cuts Paper")
            return True
        elif h.human_move == "Scissors" and c.computer_move == "Lizard":
            print("Scissors decapitates Lizard")
            return True
        elif h.human_move == "Scissors" and c.computer_move == "Spock":
            print("Spock smashes Scissors")
            return False

        # if human picks lizard
        elif h.human_move == "Lizard" and c.computer_move == "Rock":
            print("Rock crushes Lizard")
            return False
        elif h.human_move == "Lizard" and c.computer_move == "Paper":
            print("Lizard eats Paper")
            return True
        elif h.human_move == "Lizard" and c.computer_move == "Scissors":
            print("Scissors decapitates Lizard")
            return False
        elif h.human_move == "Lizard" and c.computer_move == "Spock":
            print("Lizard poisons Spock")
            return True

        #if human picks Spock
        elif h.human_move == "Spock" and c.computer_move == "Rock":
            print("Spock vaporizes Rock")
            return True
        elif h.human_move == "Spock" and c.computer_move == "Paper":
            print("Paper disproves Spock")
            return False
        elif h.human_move == "Spock" and c.computer_move == "Scissors":
            print("Spock smashes Scissors")
            return True
        elif h.human_move == "Spock" and c.computer_move == "Lizard":
            print("Lizard poisons Spock")
            return False