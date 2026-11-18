from display import show_instructions
from game import play_game

def main():
    replay_game = True 
    show_instructions()

    while replay_game:
        play_game()
        replay = input("Would you like to play again? (yes/no): ")

        while replay.lower() != "yes" and replay.lower() != "no":
            print("Invalid input. Please enter yes or no")
            replay = input("Would you like to play again? (yes/no): ")
    
        if replay.lower() == "no":
            replay_game = False

if __name__ == "__main__":
    main()
    