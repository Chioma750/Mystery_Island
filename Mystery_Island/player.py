def create_player():
    player_name = input("What is your name: ")

    player = {
        "name": player_name,
        "energy": 5,
        "location": "Beach",
        "inventory": []
    }
    return player