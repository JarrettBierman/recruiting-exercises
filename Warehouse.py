class Warehouse:
    def __init__(self):
        self.name = "test warehouse"
        self.inventory = {}
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory
    def __str__(self):
        return f"{{name: {self.name}, inventory: {self.inventory}}}"
    def __repr__(self):
        return f"{{name: {self.name}, inventory: {self.inventory}}}"
