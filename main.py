from run_game import Run_game


run_game = Run_game()
run_game.display_welcome()

#single player mode
if run_game.single_or_two_player() == True:
    
    computer_counter = 0
    human_counter = 0
    round_number = 1
    while computer_counter < 2 and human_counter < 2:
        print(f"\nRound: {round_number}")
        round = run_game.single_player_round()
        if round == False:
            computer_counter += 1
        elif round == True:
            human_counter += 1
        elif round == "Tie":
            print("It's a Tie")
        print(f"\nComputer score: {computer_counter}")
        print(f"Human score: {human_counter}")
        round_number += 1

    if computer_counter == 2:
        print("Computer Wins!")
    if human_counter == 2:
        print("Human Wins!!")

