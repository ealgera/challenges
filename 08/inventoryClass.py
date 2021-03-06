class Inventory():

    class Items():

        def __init__(self, itn, itc):
            self.itemname = itn
            self.itemcost = itc

        def show(self, i):
            print(f"\t{str(i+1).zfill(2)}: {self.itemname.ljust(15, '.')} Cost: {float(self.itemcost):7.2f}")


    def __init__(self, rn):
        self.roomname = rn
        self.items = []    # A list of MyItems.

    def showInv(self):
        print(f"Room: {self.roomname} (# items - {len(self.items)})")
        if len(self.items) > 0:
            tot = 0.0
            for i, item in enumerate(self.items):
                tot += float(item.itemcost)
                item.show(i)
            s = "-------+"
            print(f"{s.rjust(42)}")
            print(str(tot).rjust(41))
        else:
            print(f"The room \'{self.roomname}\' does not have any items.")

    def addInv(self, rn):
        self.roomname = rn

    def addInvItems(self, i, c):
        t = self.Items(i, c)
        self.items.append(t)

    def delInv(self):
        pass

    def changeInv(self, r, i, ):
        pass
