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

def show_inventory(player):
    print(player["inventory"])

def show_status(player):
    print(player["name"])
    print(player["energy"])
    print(player["location"])