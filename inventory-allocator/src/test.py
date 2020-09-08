import unittest

from shipment import optimal_shipping, warehouse_purchase

class TestCase(unittest.TestCase):

	# test empty shipping list
	def test_zero(self):
		shipment_order_0 = {}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_0 = []
		result = optimal_shipping(shipment_order_0, warehouses)
		self.assertEqual(result, expected_output_0, False)

	# test 1 item purchase from 1 warehouse	
	def test_one(self):
		shipment_order_1 = {"apple": 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_1 = [{'owd': {'apple': 1}}]
		result = optimal_shipping(shipment_order_1, warehouses)
		self.assertEqual(result, expected_output_1, False)

	# test multiple item purchase from 1 warehouse
	def test_two(self):
		shipment_order_2 = {"apple": 1, "mango": 1, "potato": 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_2 = [{'owd': {'apple': 1, 'mango': 1, 'potato': 1}}]
		result = optimal_shipping(shipment_order_2, warehouses)
		self.assertEqual(result, expected_output_2, False)

	# test multiple item purchase from multiple warehouses	
	def test_three(self):
		shipment_order_3 = {"apple": 1, "mango": 2, "potato": 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_3 = [{'owd': {'apple': 1, 'mango': 1, 'potato': 1}}, {'dm': {'mango': 1}}]
		result = optimal_shipping(shipment_order_3, warehouses)
		self.assertEqual(result, expected_output_3, False)

	# test purchase of items not available in any warehouse
	def test_four(self):
		shipment_order_4 = {"apple": 1, "mango": 2, "cantaloupe": 4}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_4 = []
		result = optimal_shipping(shipment_order_4, warehouses)
		self.assertEqual(result, expected_output_4, False)

	# test purchase of items when first item has 0 quantity in shipping list
	def test_five(self):
		shipment_order_5 = {"apple": 0, "mango": 2, "potato": 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_5 = [{'owd': {'mango': 1, 'potato': 1}}, {'dm': {'mango': 1}}]
		result = optimal_shipping(shipment_order_5, warehouses)
		self.assertEqual(result, expected_output_5, False)

	# test purchase of items not available in sufficient quantity in warehouses
	def test_six(self):
		shipment_order_6 = {"apple": 12, "mango": 1}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_6 = []
		result = optimal_shipping(shipment_order_6, warehouses)
		self.assertEqual(result, expected_output_6, False)

	# test purchase of items when last item has 0 quantity
	def test_seven(self):
		shipment_order_7 = {"apple": 7, "mango": 0}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_7 = [{'owd': {'apple': 6}}, {'dm': {'apple': 1}}]
		result = optimal_shipping(shipment_order_7, warehouses)
		self.assertEqual(result, expected_output_7, False)

	# test purchase of items when center item has 0 quantity in shipping list
	def test_eight(self):
		shipment_order_8 = {"apple": 9, "potato": 0, "mango": 2}
		warehouses = [{ "name": "owd", "inventory": { "apple": 6,"mango": 1, "potato": 1} }, 
    				{ "name": "oz", "inventory": {}}, { "name": "dm", "inventory": { "apple": 5, "mango": 1} }]
		expected_output_8 = [{'owd': {'apple': 6, 'mango': 1}}, {'dm': {'apple': 3, 'mango': 1}}]
		result = optimal_shipping(shipment_order_8, warehouses)
		self.assertEqual(result, expected_output_8, False)


if __name__ == '__main__':
	unittest.main()

