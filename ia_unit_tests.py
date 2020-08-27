from Warehouse import Warehouse
from InventoryAllocator import InventoryAllocator
import unittest

class IATester(unittest.TestCase):
    def test_public_1(self):
        order = {"apple" : 1}
        warehouses = [Warehouse("owd", {"apple" : 1})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = "[{name: owd, inventory: {'apple': 1}}]"
        self.assertEqual(str(ia.generate_shipment()), expected_output)

    def test_public_2(self):
        order = {"apple" : 10}
        warehouses = [Warehouse("owd", {"apple" : 5}), Warehouse("dm", {"apple" : 5})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = "[{name: owd, inventory: {'apple': 5}}, {name: dm, inventory: {'apple': 5}}]"
        self.assertEqual(str(ia.generate_shipment()), expected_output)

    def test_public_3(self):
        order = {"apple" : 1}
        warehouses = [Warehouse("owd", {"apple" : 0})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = "[]"
        self.assertEqual(str(ia.generate_shipment()), expected_output)

    def test_public_4(self):
        order = {"apple" : 2}
        warehouses = [Warehouse("owd", {"apple" : 1})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = "[]"
        self.assertEqual(str(ia.generate_shipment()), expected_output)
###############################################################################

    # base case 1
    def test_private_1(self):
        order = {"a" : 6, "b" : 7, "c" : 5}
        warehouses = [Warehouse("w1", {"a" : 5, "b" : 7}), Warehouse("w2", {"a" : 6, "c" : 5})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = "[{name: w1, inventory: {'a': 5, 'b': 7}}, {name: w2, inventory: {'a': 1, 'c': 5}}]"
        self.assertEqual(str(ia.generate_shipment()), expected_output)

    # edge case: you don't need any more of item a from w3, so there should be no shipments from w3
    def test_private_2(self):
        order = {"a" : 15}
        warehouses = [Warehouse("w1", {"a" : 5, "b" : 2, "c" : 1}), Warehouse("w2", {"a" : 10, "b" : 4}), Warehouse("w3", {"a" : 4, "c" : 3})]
        ia = InventoryAllocator(order, warehouses)
        expected_output = "[{name: w1, inventory: {'a': 5}}, {name: w2, inventory: {'a': 10}}]"
        self.assertEqual(str(ia.generate_shipment()), expected_output)

# main method
if __name__ == '__main__':
    unittest.main()



