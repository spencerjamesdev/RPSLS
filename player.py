class Player:

    def __init__(self, name):
        self.name = name
        self.chosen_gesture = None
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.wins = 0
        self.winning_matchups = []

    def add_win(self):
        self.wins += 1

    def winning_matches(self, gesture):
        if gesture == 1:
            self.winning_matchups.append(3)
            self.winning_matchups.append(4)
        if gesture == 2:
            self.winning_matchups.append(1)
            self.winning_matchups.append(5)
        if gesture == 3:
            self.winning_matchups.append(2)
            self.winning_matchups.append(4)
        if gesture == 4:
            self.winning_matchups.append(2)
            self.winning_matchups.append(5)
        if gesture == 5:
            self.winning_matchups.append(1)
            self.winning_matchups.append(3)
