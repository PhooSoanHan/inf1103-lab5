import json
import os


def load_inventory():
    if os.path.exists("inventory.json"):
        print("inventory.json found.")

        with open("inventory.json", "r") as file:
            inventory = json.load(file)

        print("Inventory loaded successfully.")
        return inventory

    else:
        print("inventory.json not found.")
        print("Starting with empty inventory.")
        return []


inventory = load_inventory()