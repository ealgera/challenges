class Indenter:
    
    def __init__(self):
        self.spaces = -1
        self.indenttxt = ""
        self.deftxt = "...."

    def __enter__(self):
        self.spaces += 1
        self.indenttxt = self.deftxt * self.spaces
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.spaces -= 1
        self.indenttxt = self.deftxt * self.spaces

    def print(self, txt):
        print(self.indenttxt + txt)