from player import create_player
from locations import locations
from actions import explore_location, restore_beacon
from display import show_inventory, show_status

def play_game():
    player = create_player()

    game_running = True

    while game_running:
        print("1. Explore location")
        print("2. View Inventory")
        print("3. View Player Status")
        print("4. Restore Beacon")
        print("5. Quit Game")

        choice = input("Enter a choice from 1 to 5: ")

        if choice == "1":
            if not explore_location(player, locations):
                game_running = False 
        elif choice == "2":
            show_inventory(player)
            print()
        elif choice == "3":
            show_status(player)
            print()
        elif choice == "4":
            if restore_beacon(player):
                game_running = False
                print()
        elif choice == "5":
            game_running = False
            print("Quitting...")
            print()
        else:
            print("Invalid input, choose from 1 to 5.")