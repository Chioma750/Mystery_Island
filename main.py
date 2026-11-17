def show_instructions():
    print("=== MYSTERY ISLAND: THE RESCUE MISSION ===")
    print()
    print("=== INSTRUCTIONS ===")
    print("You are stranded on a mysterious island, and need to collect a Rope and a Lantern.")
    print("All you need to do is:")
    print("1. Collect the Rope and the Lantern")
    print("2. You need the Rope to cross the Old Bridge")
    print("3. You need the Lantern to restore the Lighthouse beacon.")
    print("4. You start with 5 energy points, and each successful movement costs 1 energy point.")
    print("5. Restore the beacon to bring the rescue boat.")
    print()
show_instructions()

locations = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}

replay_game = True 

while replay_game:
def create_player():
    player_name = input("What is your name: ")

    player = {
        "name": player_name,
        "energy": 5,
        "location": "Beach",
        "inventory": []
    }
    return player

    game_running = True

    while game_running:
        print("1. Explore location")
        print("2. View Inventory")
        print("3. View Player Status")
        print("4. Restore Beacon")
        print("5. Quit Game")

        choice = input("Enter a choice from 1 to 5: ")

        if choice == "1":
            print(player["location"]) 
            # Nested dictionary access.
            print(locations[player["location"]])

            destination = input("Where would you like to go: ")

            if destination in locations[player["location"]]:
            
                if destination == "Old Bridge" and "Rope" not in player["inventory"]:
                    print("A Rope is required to cross the Old Bridge.")
                else:
                    player["location"] = destination

                    if player["location"] == "Jungle" and "Rope" not in player["inventory"]:
                        player["inventory"].append("Rope")
                        print("You have collected the Rope!")

                    if player["location"] == "Cave" and "Lantern" not in player["inventory"]:
                        player["inventory"].append("Lantern")
                        print("You have collected the Lantern!")

                    player["energy"] -= 1

                    if player["energy"] == 0:
                        game_running = False
                        print("You have run out of energy, Game Over!")
            else:
                print("You cannot travel there from this location.")

def show_inventory(player):
    print(player["inventory"])

def show_status(player):
    print(player["name"])
    print(player["energy"])
    print(player["location"])

def restore_beacon(player):
    if player["location"] == "Lighthouse" and "Lantern" in player["inventory"]:
        print("Beacon Restored Successfully")
        print("Congratulations! The rescue boat has found you!")
        return True
    else:
        print("You do not have a Lantern. The beacon cannot be restored.")
        return False

        elif choice == "5":
            game_running = False
            print("Quitting...")
            # break
            
        else:
            print("Invalid input, choose from 1 to 5.")

    replay = input("Would you like to play again? (yes/no): ")

    while replay.lower() != "yes" and replay.lower() != "no":
        print("Invalid input. Please enter yes or no")
        replay = input("Would you like to play again? (yes/no): ")
    
    if replay.lower() == "no":
        replay_game = False
    