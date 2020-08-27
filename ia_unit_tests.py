from Warehouse import Warehouse
from InventoryAllocator import InventoryAllocator
import unittest

class IATester(unittest.TestCase):
    # public test: one warehouse ships all of one item
    def test_public_1(self):
        order = {"apple" : 1}
        warehouses = [Warehouse("owd", {"apple" : 1})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = [Warehouse("owd", {"apple": 1})]
        self.assertEqual(ia.generate_shipment(), expected_output)

    # public test: two warehouses ship all of one item
    def test_public_2(self):
        order = {"apple" : 10}
        warehouses = [Warehouse("owd", {"apple" : 5}), Warehouse("dm", {"apple" : 5})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = [Warehouse("owd", {"apple" : 5}), Warehouse("dm", {"apple" : 5})]
        self.assertEqual(ia.generate_shipment(), expected_output)

    # public test: not enough inventory: order does not ship
    def test_public_3(self):
        order = {"apple" : 1}
        warehouses = [Warehouse("owd", {"apple" : 0})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = []
        self.assertEqual(ia.generate_shipment(), expected_output)

    # public test: not enough inventory: order does not ship
    def test_public_4(self):
        order = {"apple" : 2}
        warehouses = [Warehouse("owd", {"apple" : 1})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = []
        self.assertEqual(ia.generate_shipment(), expected_output)

    # base case with large quantities
    def test_private_base(self):
        order = {"playstation" : 1000}
        warehouses = []
        for i in range(600):
            warehouses.append(Warehouse(f"w-{i}", {"playstation" : 2, "xbox" : 1}))
        ia = InventoryAllocator(order, warehouses)
        expected_output = []
        for i in range(500):
            expected_output.append(Warehouse(f"w-{i}", {"playstation" : 2}))
        self.assertEqual(ia.generate_shipment(), expected_output)

    # edge case: two warehouses ship three items with inventory left over
    def test_private_inv_left_over(self):
        order = {"a" : 6, "b" : 7, "c" : 5}
        warehouses = [Warehouse("w1", {"a" : 5, "b" : 7}), Warehouse("w2", {"a" : 6, "c" : 5})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = [Warehouse("w1", {"a" : 5, "b" : 7}), Warehouse("w2", {"a":1, "c":5})]
        self.assertEqual(ia.generate_shipment(), expected_output)

    # edge case: you don't need any more of item a from w3, so there should be no shipments from w3
    def test_private_extra_warehouse(self):
        order = {"a" : 15}
        warehouses = [Warehouse("w1", {"a" : 5, "b" : 2, "c" : 1}), Warehouse("w2", {"a" : 10, "b" : 4}), Warehouse("w3", {"a" : 4, "c" : 3})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = [Warehouse("w1", {"a" : 5}), Warehouse("w2", {"a" : 10})]
        self.assertEqual(ia.generate_shipment(), expected_output)

    # edge case: 2 warehouses split an order with two items and not all of the inventory is needed
    def test_private_inv_left_over_2(self):
        order = {"a" : 5, "b" : 6}
        warehouses = [Warehouse("w1", {"a" : 6, "b" : 2}), Warehouse("w2", {"b" : 4})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = [Warehouse("w1", {"a" : 5, "b" : 2}), Warehouse("w2", {"b" : 4})]
        self.assertEqual(ia.generate_shipment(), expected_output)

    # edge case: an item is in the order that does not appear in any warehouses
    def test_private_missing_item(self):
        order = {"a" : 1}
        warehouses = [Warehouse("w1", {"b" : 1})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = []
        self.assertEqual(ia.generate_shipment(), expected_output)

    # edge case: an item is in a warehouse that does not appear in the order
    def test_private_extra_warehouse_item(self):
        order = {"a" : 1}
        warehouses = [Warehouse("w1", {"a" : 1, "b" : 1})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = [Warehouse("w1", {"a": 1})]
        self.assertEqual(ia.generate_shipment(), expected_output)

    # edge case: trying to order to an empty warehouse
    def test_private_empty_warehouse(self):
        order = {"a" : 1}
        warehouses = [Warehouse("empty", {})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = []
        self.assertEqual(ia.generate_shipment(), expected_output)

    # edge case: looks through 2 warehouses, one is empty, so skips it and completes order with second warehouse
    def test_private_empty_warehouse_2(self):
        order = {"a" : 1}
        warehouses = [Warehouse("w1", {}), Warehouse("w2", {"a" : 1})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = [Warehouse("w2", {"a" : 1})]
        self.assertEqual(ia.generate_shipment(), expected_output)

    # edge case: trying to order to with an empty order
    def test_private_7(self):
        order = {}
        warehouses = [Warehouse("w1", {"a" : 1})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = []
        self.assertEqual(ia.generate_shipment(), expected_output)
    
        
    # edge case: has enough inventory for some items in order but not every item
    def test_private_9(self):
        order = {"chair" : 100, "couch" : 50, "bed" : 30}
        warehouses = []
        warehouses.append(Warehouse("w1", {"chair" : 30, "couch" : 30}))
        warehouses.append(Warehouse("w2", {"chair" : 30, "bed" : 30}))
        warehouses.append(Warehouse("w3", {"chair" : 30, "couch" : 20}))
        ia = InventoryAllocator(order, warehouses)
        expected_output = [] # not enough chairs to complete order
        self.assertEqual(ia.generate_shipment(), expected_output)
    

# main method to run tests
if __name__ == '__main__':
    unittest.main()



