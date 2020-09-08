import unittest

from shipment import optimal_shipping, warehouse_purchase

class TestCase(unittest.TestCase):

	def test_zero(self):
		shipment_order_0 = {}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_0 = []
		result = optimal_shipping(shipment_order_0, warehouses)
		self.assertEqual(result, expected_output_0, False)

	def test_one(self):
		shipment_order_1 = {"apple": 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_1 = [{'owd': {'apple': 1}}]
		result = optimal_shipping(shipment_order_1, warehouses)
		self.assertEqual(result, expected_output_1, False)

	def test_two(self):
		shipment_order_2 = {"apple": 1, "mango": 1, "potato": 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_2 = [{'owd': {'apple': 1, 'mango': 1, 'potato': 1}}]
		result = optimal_shipping(shipment_order_2, warehouses)
		self.assertEqual(result, expected_output_2, False)

	def test_three(self):
		shipment_order_3 = {"apple": 1, "mango": 2, "potato": 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_3 = [{'owd': {'apple': 1, 'mango': 1, 'potato': 1}}, {'dm': {'mango': 1}}]
		result = optimal_shipping(shipment_order_3, warehouses)
		self.assertEqual(result, expected_output_3, False)

	def test_four(self):
		shipment_order_4 = {"apple": 1, "mango": 2, "cantaloupe": 4}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_4 = []
		result = optimal_shipping(shipment_order_4, warehouses)
		self.assertEqual(result, expected_output_4, False)

	def test_five(self):
		shipment_order_5 = {"apple": 0, "mango": 2, "potato": 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_5 = [{'owd': {'mango': 1, 'potato': 1}}, {'dm': {'mango': 1}}]
		result = optimal_shipping(shipment_order_5, warehouses)
		self.assertEqual(result, expected_output_5, False)

	def test_six(self):
		shipment_order_6 = {"apple": 12, "mango": 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_6 = []
		result = optimal_shipping(shipment_order_6, warehouses)
		self.assertEqual(result, expected_output_6, False)

	def test_seven(self):
		shipment_order_7 = {"apple": 7, "mango": 0}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_7 = [{'owd': {'apple': 6}}, {'dm': {'apple': 1}}]
		result = optimal_shipping(shipment_order_7, warehouses)
		self.assertEqual(result, expected_output_7, False)


if __name__ == '__main__':
	unittest.main()

