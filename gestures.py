class Gestures:

    def __init__(self, gesture):
        self.gesture = gesture
        self.wins = []
        self.whoWins()

    def whoWins(self):
        if self.gesture == "Rock":
            self.wins.append("Scissors")
            self.wins.append("Lizard")
        if self.gesture == "Paper":
            self.wins.append("Rock")
            self.wins.append("Spock")
        if self.gesture == "Scissors":
            self.wins.append("Paper")
            self.wins.append("Lizard")
        if self.gesture == "Lizard":
            self.wins.append("Paper")
            self.wins.append("Spock")
        if self.gesture == "Spock":
            self.wins.append("Scissors")
            self.wins.append("Rock")
