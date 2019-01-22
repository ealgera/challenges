import json
from pprint import pprint
from inventoryClass import MyInventory

my_inv = []

with open('inventory.json') as f:
    rooms = json.load(f)

print()

# Read JSON elements into inventory objects
for room in rooms['Kamers']['Kamer']: # Want dit niveau is een list / iterable
    t = MyInventory(room['naam'])
    
    for item in room['items']: # Want dit niveau is een list / iterable
        t.addInvItems(item['item'], item['waarde'])

    my_inv.append(t)
#
#new_inv = MyInventory("Keuken")
#new_inv.addInvItems('Vaatwasser', 875)
#my_inv.append(new_inv)
#
new_inv = MyInventory("Bij-Keuken")
new_inv.addInvItems('Container', 75)
my_inv.append(new_inv)

print(f"Number of rooms: {len(my_inv)}")
print()

for item in my_inv:
    print(item.showInv())

print()
