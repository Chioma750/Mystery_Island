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
print(player)

game_running = True

while game_running:
    print("1. Explore location")
    print("2. View Inventory")
    print("3. View Player Status")
    print("4. Quit Game")

    choice = input("Enter a choice from 1 to 4: ")

    if choice == "2":
        player["inventory"]
    elif choice == "3":
        player["name"]
        player["energy"]
        player["location"]
    elif choice == "4":
        game_running = False
        print("Quitting...")
    else:
        print("Invalid input, choose from 1 to 4.")
        