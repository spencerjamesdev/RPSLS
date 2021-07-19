from player import Player
from human import Human
from computer import Computer

class Run_game:
    

    def __init__(self):
        
        pass

    def display_welcome(self):
        rules_input = input("Welcome to Rock, Paper, Scissors, Lizard, Spock! Would you like to see the rules? 'y' or 'n': ")
        if rules_input == "y" or "Y":
            print("Best out of 3 wins.")
            print("Rules: \nRock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock")
        if rules_input == "n" or "N":
            print("Best out of 3 wins.")
    
    #If 1 then single and true, if 2 then multiplayer and false
    def single_or_two_player(self):
        number_of_players = input("How many people are playing? 1 or 2: ")
        if number_of_players == "1":
            return True
        elif number_of_players == "2":
            return False

    def single_player_round(self):
        #instantiating human and computer objects
        h = Human()
        c = Computer()

        hm = h.human_move()
        cm = c.computer_move()
        #checking if move is a tie
        print(f"You chose {hm}. The computer chose {cm}.")
        
        if hm == cm:
            return "Tie"
        
        #if human picks rocks
        elif hm == "Rock" and cm == "Paper":
            print("Paper covers Rock")
            return False
        elif hm == "Rock" and cm == "Scissors":
            print("Rock crushes Scissors")
            return True
        elif hm == "Rock" and cm == "Lizard":
            print("Rock crushes Lizard")
            return True
        elif hm == "Rock" and cm == "Spock":    
            print("Spock vaporizes Rock")
            return False
        
        #if human picks paper
        elif hm == "Paper" and cm == "Rock":
            print("Paper covers Rock")
            return True
        elif hm == "Paper" and cm == "Scissors":
            print("Scissors cuts Paper")
            return False
        elif hm == "Paper" and cm == "Lizard":
            print("Lizard eats Paper")
            return False
        elif hm == "Paper" and cm == "Spock":
            print("Paper disproves Spock")
            return True

        #if human picks Scissors
        elif hm == "Scissors" and cm == "Rock":
            print("Rock crushes Scissors")
            return False
        elif hm == "Scissors" and cm == "Paper":
            print("Scissors cuts Paper")
            return True
        elif hm == "Scissors" and cm == "Lizard":
            print("Scissors decapitates Lizard")
            return True
        elif hm == "Scissors" and cm == "Spock":
            print("Spock smashes Scissors")
            return False

        # if human picks lizard
        elif hm == "Lizard" and cm == "Rock":
            print("Rock crushes Lizard")
            return False
        elif hm == "Lizard" and cm == "Paper":
            print("Lizard eats Paper")
            return True
        elif hm == "Lizard" and cm == "Scissors":
            print("Scissors decapitates Lizard")
            return False
        elif hm == "Lizard" and cm == "Spock":
            print("Lizard poisons Spock")
            return True

        #if human picks Spock
        elif hm == "Spock" and cm == "Rock":
            print("Spock vaporizes Rock")
            return True
        elif hm == "Spock" and cm == "Paper":
            print("Paper disproves Spock")
            return False
        elif hm == "Spock" and cm == "Scissors":
            print("Spock smashes Scissors")
            return True
        elif hm == "Spock" and cm == "Lizard":
            print("Lizard poisons Spock")
            return False

