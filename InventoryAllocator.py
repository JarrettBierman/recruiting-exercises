from Warehouse import Warehouse

class InventoryAllocator:
    
    def __init__(self, order, warehouses):
        self.order = order
        self.warehouses = warehouses
    
    # REQUIRES: valid order map and list of warehouse objects
    # EFFECTS: takes in the order map and the list of warehouses and returns
    # a list of warehouses 
    def generate_shipment(self):
        ret = []
        order_copy = self.order                                     # create a copy of orders to not lose data
        order_items = list(order_copy.keys())
        for warehouse in self.warehouses:                           # check each warehouse
            temp_dict = {}                                          # what this warehouse will give
            for item in order_items:                                # check each item we need to get
                if not warehouse.inventory.get(item):               #check if item exists in the warehouse inventory
                    continue
                if order_copy[item] > warehouse.inventory[item]:    # if the warehouse does not have enough of the item 
                    temp_dict[item] = warehouse.inventory[item]     # take all of them
                    order_copy[item] -= warehouse.inventory[item]   
                else:                                               # there are more items in the warehouse than needed in the order
                    temp_dict[item] = order_copy[item]
                    order_copy[item] = 0
            for key in order_copy:                                  # checks and removes warehouse items that ship a quantity of 0
                if temp_dict.get(key) == 0:
                    del temp_dict[key]
            if bool(temp_dict):                                     # checks if temp_dict is not empty. If it is, do not add it to the return
                ret.append(Warehouse(warehouse.name, temp_dict))
        for key in order_copy:                                      # checks to see if the order is complete. An incomplete 
            if order_copy[key] > 0:                                 # order cannot be shipped, so if there are still items left,
                return []                                           # we will return an empty list
        return ret

