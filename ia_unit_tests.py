from Warehouse import Warehouse
from InventoryAllocator import InventoryAllocator

# Helper function to output the results of the unit tests
def unit_test(order, warehouses, expected_output):
    ia = InventoryAllocator(order, warehouses)
    real_output = str(ia.generate_shipment())
    print(f"order:              {order}")
    print(f"warehouses:         {warehouses}")
    print(f"expected output:    {expected_output}")
    print(f"actual output:      {real_output}")
    print(f"expected == actual: {expected_output == real_output}")
    print()


# Public Test 1: Happy Case, Order can be shipped using one warehouse
print("Public Test 1: Happy Case, Order can be shipped using one warehouse")
order = {"apple" : 1}
warehouses = [Warehouse("owd", {"apple" : 1})]
expected_output = "[{name: owd, inventory: {'apple': 1}}]"
unit_test(order, warehouses, expected_output)

# Public Test 2: Order can be shipped using multiple warehouses
print("Public Test 2: Order can be shipped using multiple warehouses")
order = {"apple" : 10}
warehouses = [Warehouse("owd", {"apple" : 5}), Warehouse("dm", {"apple" : 5})]
expected_output = "[{name: owd, inventory: {'apple': 5}}, {name: dm, inventory: {'apple': 5}}]"
unit_test(order, warehouses, expected_output)


# Public Test 3: Order cannot be shipped because there is not enough inventory
print("Public Test 3: Order cannot be shipped because there is not enough inventory")
order = {"apple" : 1}
warehouses = [Warehouse("owd", {"apple" : 0})]
expected_output = "[]"
unit_test(order, warehouses, expected_output)

# Public Test 4: Order cannot be shipped because there is not enough inventory
print("Public Test 4: Order cannot be shipped because there is not enough inventory")
order = {"apple" : 2}
warehouses = [Warehouse("owd", {"apple" : 1})]
expected_output = "[]"
unit_test(order, warehouses, expected_output)


