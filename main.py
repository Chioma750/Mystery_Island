locations = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}

player_name = input("What is your name: ")

player = {
    "name": player_name,
    "energy": 5,
    "location": "Beach",
    "inventory": []
}

game_running = True

while game_running:
    print("1. Explore location")
    print("2. View Inventory")
    print("3. View Player Status")
    print("4. Quit Game")

    choice = input("Enter a choice from 1 to 4: ")

    if choice == "1":
        print(player["location"]) 
        # Nested dictionary access.
        print(locations[player["location"]])

        destination = input("Where would you like to go: ")

        if destination in locations[player["location"]]:
            player["location"] = destination

            if player["location"] == "Jungle" and "Rope" not in player["inventory"]:
                player["inventory"].append("Rope")
                print("You have collected the Rope!")
            
            player["energy"] -= 1
            if player["energy"] == 0:
                game_running = False
                print("You have run out of energy, Game Over!")
        else:
            print("You cannot travel there from this location.")

    elif choice == "2":
        print(player["inventory"])
    elif choice == "3":
        print(player["name"])
        print(player["energy"])
        print(player["location"])
    elif choice == "4":
        game_running = False
        print("Quitting...")
    else:
        print("Invalid input, choose from 1 to 4.")
     