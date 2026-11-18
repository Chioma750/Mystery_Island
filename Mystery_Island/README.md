# Mystery_Island

Mystery Island is a Python text-based adventure game where the player wakes up stranded on an island after a storm with limited energy. To win and escape, the player must explore five distinct locations, gather key items like the Rope and Lantern, and make smart choices to cross a locked bridge. Their main objective is to reach the dark lighthouse and relight its beacon so a rescue boat will arrive before they run out of energy.  

## How to Run
```
python3 main.py
```

## Game Rules

* Starting Energy: You begin the game with 5 energy points.
* Navigating the Island: You can only move between connected locations, so pay close attention to the available paths from where you are standing.
* Movement Cost: Every successful move between locations costs 1 energy point, so  plan your route carefully.
* Collecting Items: You must explore the island to gather two essential tools: find the Rope in the Jungle and the Lantern in the Cave.
* Crossing the Bridge: You cannot cross the Old Bridge without the Rope in your inventory.
* Winning the Game: To win and signal the rescue boat, you must reach the Lighthouse with the Lantern to restore its beacon.
* Game Over: If your energy reaches 0 before you relight the beacon, the game ends and it is Game Over.

## Running Tests

This project uses Python's built-in unittest framework to test the game functions.

To run all tests, open your terminal in the project folder and execute:
```
python3 -m unittest discover -s tests -v
```
The command discovers and runs all test files inside the tests directory and displays detailed results.

## Known Limitations

* Text Only (No Pictures): You play the entire game by reading words and typing choices on your screen. There are no pictures, animations, or sounds.
* Automatic Item Pickups: You do not need to search around or type a command to grab items. As soon as you walk into the Jungle or the Cave, the game picks up the tool for you automatically.
* No Saving: The game does not remember your progress after you close it. If you exit the window, you will have to start over from the beginning next time.
