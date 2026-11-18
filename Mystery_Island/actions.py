def explore_location(player, locations):
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
                print("You have run out of energy, Game Over!")
                return False
    else:
        print("You cannot travel there from this location.")
    return True


def restore_beacon(player):
    if player["location"] == "Lighthouse" and "Lantern" in player["inventory"]:
        print("Beacon Restored Successfully")
        print("Congratulations! The rescue boat has found you!")
        return True
    elif "Lantern" not in player["inventory"]:
        print("You do not have a Lantern. The beacon cannot be restored.")
        return False
    else:
        print("Player has the Lantern but isn't at the Lighthouse.")
        return False