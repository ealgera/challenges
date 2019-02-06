import json
from pprint import pprint

print("Oude versie:")
print()
with open('inventory.json') as f:
    rooms = json.load(f)
pprint(rooms)

print()
print("Nieuwe versie:")
print()
with open('inventory_new.json') as f:
    rooms = json.load(f)
pprint(rooms)