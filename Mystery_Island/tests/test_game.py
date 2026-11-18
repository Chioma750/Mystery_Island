# python -m unittest discover -s tests -v
import unittest
from unittest.mock import patch

from player import create_player
from actions import explore_location, restore_beacon
from locations import locations

class TestCreatePlayer(unittest.TestCase):

    @patch("builtins.input", return_value="Chioma")
    def test_create_player(self, mock_input):
        player = create_player()

        self.assertEqual(player["name"], "Chioma")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["inventory"], [])


class TestRestoreBeacon(unittest.TestCase):

    def test_restore_beacon_success(self):
        player = {
            "location": "Lighthouse",
            "inventory": ["Rope", "Lantern"]
        }

        result = restore_beacon(player)

        self.assertTrue(result)

    def test_restore_beacon_without_lantern(self):
        player = {
            "location": "Lighthouse",
            "inventory": ["Rope"]
        }

        result = restore_beacon(player)

        self.assertFalse(result)

    def test_restore_beacon_wrong_location(self):
        player = {
            "location": "Beach",
            "inventory": ["Rope", "Lantern"]
        }

        result = restore_beacon(player)

        self.assertFalse(result)


class TestExploreLocation(unittest.TestCase):

    def test_successful_movement(self):
        player = {
            "location": "Beach",
            "energy": 5,
            "inventory": []
        }

        with patch("builtins.input", return_value="Jungle"):
            result = explore_location(player, main.locations)

        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)
        self.assertIn("Rope", player["inventory"])
        self.assertTrue(result)

    def test_invalid_destination(self):
        player = {
            "location": "Beach",
            "energy": 5,
            "inventory": []
        }

        with patch("builtins.input", return_value="Cave"):
            result = explore_location(player, main.locations)

        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)
        self.assertTrue(result)

    def test_energy_reaches_zero(self):
        player = {
            "location": "Beach",
            "energy": 1,
            "inventory": []
        }

        with patch("builtins.input", return_value="Jungle"):
            result = explore_location(player, main.locations)

        self.assertEqual(player["energy"], 0)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
