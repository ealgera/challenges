import json
from pprint import pprint
from inventoryClass import Inventory

class Inventories():

    def __init__(self):
        self.inventory_list = []
        self.cur = 0

    def __len__(self):
        return len(self.inventory_list)

    def __iter__(self):
        return self

    def __next__(self):
        i = self.cur
        if i >= len(self.inventory_list):
            raise StopIteration
        self.cur += 1
        return self.inventory_list[i]

    def load_inventory(self, fname):
        # Read JSON elements into inventory objects
        with open(fname) as f:
            rooms = json.load(f)

        for room in rooms['Kamers']['Kamer']: # Want dit niveau is een list / iterable
            t = Inventory(room['naam'])
    
            for item in room['items']: # Want dit niveau is een list / iterable
                t.addInvItems(item['item'], item['waarde'])

            self.inventory_list.append(t)

    def write_inventory(self):
        with open('temp.json', 'w') as f:
            json.dump(self.inventory_list, f)

    def add_inventory(self, name, item, cost):
        i = self.search_inventory(name) 
        if  i >= 0:
            print(f"Kamer {name} gevonden! Toevoegen items: {item}, waarde is {cost}")
            self.inventory_list[i].addInvItems(item, cost)
        else:
            print(f"Kamer {name} niet gevonden, wordt toegevoegd...")
            tmp = Inventory(name)
            tmp.addInvItems(item, cost)
            self.inventory_list.append(tmp)

    def search_inventory(self, n):
        for i, item in enumerate(self.inventory_list):
            #print(i, item)
            if item.roomname == n:
                return i
        return -1

    def show(self):
        print()
        print(f"Number of rooms: {len(self.inventory_list)}")
        print()
        for inventory in self.inventory_list:
            print(inventory.showInv()) 

    def print_total(self):
        total = 0.0
        for inventory in self.inventory_list:
            for item in inventory.items:
                total += float(item.itemcost)
        print()
        print(f"Totale waarde is: {str(total).rjust(23)}")
        t = "="*8
        print(t.rjust(41))
        print()
