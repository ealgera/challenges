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
        i = MyInventory.MyItems(item['item'], item['waarde'])
        t.addInvItems(i)

    my_inv.append(t)

new_inv = MyInventory("Bij-Keuken")
my_inv.append(new_inv)

print(f"Number of rooms: {len(my_inv)}")
print()

for item in my_inv:
    print(item.showInv())

print()
