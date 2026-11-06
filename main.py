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