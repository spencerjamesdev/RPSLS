from os import system, name
from player import Player
from computer import Computer
from human import Human


class Game:

    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")

    def start(self):
        self.clear()
        print("\n** Welcome to Rock Paper Scissors Lizard Spock **\n")
        print("Rules: \nRock crushes Scissors \nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporizes Rock\n")
        input("Press any key to continue. . .")
        self.clear()
        self.game_type()

    def game_type(self):
        user_input = int(input("Enter 1 for Vs AI : Enter 2 for Vs Human: "))
        while user_input != 1 and user_input != 2:
            user_input = int(
                input("Invalid Entry. Enter 1 for Vs AI : Enter 2 for Vs Human: "))
        if user_input == 1:
            self.player1 = Human("Player 1")
            self.player2 = Computer("Player 2")
            self.clear()
            self.play_game()
        else:
            self.player1 = Human("Player 1")
            self.player2 = Human("Player 2")
            self.clear()
            self.play_game()

    def play_game(self):
        while self.player1.wins < 2 and self.player2.wins < 2:
            self.clear()
            self.player1.choose_gesture()
            self.player2.choose_gesture()
            self.show_gestures()
            self.compare_gestures()
            self.show_wins()
            input("\nPress any button to continue. . .")
        self.announce_winner()
        input("\nPress any button to continue. . .")
        self.start()

    def show_gestures(self):
        print("\n" + self.player1.name + " used " +
              self.player1.gesture_list[self.player1.chosen_gesture - 1])
        print(self.player2.name + " used " +
              self.player2.gesture_list[self.player2.chosen_gesture - 1] + "\n")

    def compare_gestures(self):
        if self.player1.chosen_gesture == self.player2.chosen_gesture:
            print("It's a tie!")
            return
        won = False
        for gesture in self.player1.winning_matchups:
            if gesture == self.player2.chosen_gesture:
                won = True
        if won == True:
            print(self.player1.name + " has won the round!")
            self.player1.add_win()
        else:
            print(self.player2.name + " has won the round!")
            self.player2.add_win()

    def show_wins(self):
        print(self.player1.name + " - " + str(self.player1.wins) + " wins.")
        print(self.player2.name + " - " + str(self.player2.wins) + " wins.")

    def announce_winner(self):
        self.clear()
        if self.player1.wins > self.player2.wins:
            print("Congradulations!!!\n" +
                  self.player1.name + " has won the battle!")
        else:
            print("Congradulations!!!\n" +
                  self.player2.name + " has won the battle!")

    def clear(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")
