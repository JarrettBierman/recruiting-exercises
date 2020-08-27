class Warehouse:
    # default ctor
    def __init__(self):
        self.name = "test warehouse"
        self.inventory = {}

    # preferred ctor
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory


    # overrides the == operator
    def __eq__(self, other):
        return self.name == other.name and self.inventory == other.inventory
    
    #to string functions for correct test outputs
    def __str__(self):
        return f"{{name: {self.name}, inventory: {self.inventory}}}"

    def __repr__(self):
        return f"{{name: {self.name}, inventory: {self.inventory}}}"
