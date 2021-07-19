from player import Player
import getpass


class Human(Player):

    def __init__(self, name):
        super().__init__(name)

    def choose_gesture(self):
        print("\nGestures List:\n1. Rock\n2. Paper\n3. Scissors\n4. Lizard\n5. Spock\n")
        gesture = int(getpass.getpass(
            self.name + ", please pick a gesture, 1 - 5: "))
        while gesture < 1 or gesture > 5:
            gesture = int(input("Invalid Entry. " + self.name +
                          ", please pick a gesture, 1 - 5: "))
        self.chosen_gesture = gesture
        self.winning_matches(self.chosen_gesture)
