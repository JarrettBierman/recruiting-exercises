from Warehouse import Warehouse

class InventoryAllocator:
    
    def __init__(self, order, warehouses):
        self.order = order
        self.warehouses = warehouses

    def generate_shipment(self):
        ret = []
        order_items = list(self.order.keys())
        for warehouse in self.warehouses:                           # check each warehouse
            temp_dict = {}                                          # what this warehouse will give
            for item in order_items:                                # check each item we need to get
                if not warehouse.inventory.get(item):               #check if item exists in the warehouse inventory
                    continue
                if self.order[item] > warehouse.inventory[item]:    # if the warehouse does not have enough of the item 
                    temp_dict[item] = warehouse.inventory[item]     # take all of them
                    self.order[item] -= warehouse.inventory[item]   # E
                else:                                               # there are more items in the warehouse than needed in the order
                    temp_dict[item] = self.order[item]
                    self.order[item] = 0
            if bool(temp_dict):                                     # checks if temp_dict is not empty. If it is, do not add it to the return
                ret.append(Warehouse(warehouse.name, temp_dict))
        for key in self.order:                                      # checks to see if the order is complete. An incomplete order cannot be shipped, so if there are still items left, we will return an empty list
            if self.order[key] > 0:
                return []
        return ret

