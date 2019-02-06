from InventoriesClass import Inventories
from pprint import pprint

my_inv = Inventories()
my_inv.load_inventory('inventory.json')

#Bestaande kamers
my_inv.add_inventory("Keuken", "Vaatwasser", 875)
my_inv.add_inventory("Woonkamer", "Kussen", 5)
my_inv.add_inventory("Keuken", "Pannenset", 199)

#Niet bestaande kamers
my_inv.add_inventory("Kelder", "Oude fiets", 2)
my_inv.add_inventory("Bijkeuken", "Afvalemmer", 10.99)

my_inv.show()
#my_inv.print_total()


my_inv.save_inventory('inventory_new.json')