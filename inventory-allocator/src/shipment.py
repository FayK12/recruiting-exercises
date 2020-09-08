
def warehouse_purchase(shipment_order, warehouse_inventory, purchased, clear_shipment_order):
  
  for fruit in shipment_order:
    if shipment_order[fruit] == 0:
      clear_shipment_order.add(fruit)
    if fruit in shipment_order and fruit in warehouse_inventory and warehouse_inventory[fruit] > 0 and shipment_order[fruit] > 0:
      available = warehouse_inventory[fruit]
      if (shipment_order[fruit] > available):
          shipment_order[fruit] -= available
          purchased[fruit] = available
      else:
        purchased[fruit] = shipment_order[fruit]
        shipment_order[fruit] = 0
        clear_shipment_order.add(fruit)
        
  return shipment_order, purchased, clear_shipment_order


def optimal_shipping(shipment_order, warehouses):

    checkout = []

    if len(shipment_order) == 0:
      return checkout

    for i in range(len(warehouses)):
      
      name = warehouses[i]['name']
      warehouse_inventory = warehouses[i]['inventory']
      purchased = {}
      warehouse_items = {}
      clear_shipment_order = set()
      
      if len(warehouse_inventory) > 0 and len(shipment_order) > 0:
        shipment_order, purchased, clear_shipment_order = warehouse_purchase(shipment_order, warehouse_inventory, purchased, clear_shipment_order)
        
        if len(clear_shipment_order) > 0:
          for fruit in clear_shipment_order:
            del shipment_order[fruit]

        if len(purchased) > 0:
          warehouse_items[name] = purchased
          checkout.append(warehouse_items)
          
    if len(shipment_order) > 0:
      checkout = []

    return checkout

      
warehouses = [{
        "name": "FreshCo",
        "inventory": {
            "apple": 6,
            "mango": 1,
            "potato": 1
    }
    }, 
    {
        "name": "XYZ",
        "inventory": {}
    },
    {
        "name": "NoFrills",
        "inventory": {
            "apple": 5,
            "mango": 1
    }
    }]


shipment_order_0 = {}
expected_output_0 = []
print("0", optimal_shipping(shipment_order_0, warehouses) == expected_output_0)

shipment_order_1 = {"apple": 1}
expected_output_1 = [{'FreshCo': {'apple': 1}}]
print("1",optimal_shipping(shipment_order_1, warehouses) == expected_output_1)

shipment_order_2 = {"apple": 1, "mango": 1, "potato": 1}
expected_output_2 = [{'FreshCo': {'apple': 1, 'mango': 1, 'potato': 1}}]
print("2", optimal_shipping(shipment_order_2, warehouses) == expected_output_2)

shipment_order_3 = {"apple": 1, "mango": 2, "potato": 1}
expected_output_3 = [{'FreshCo': {'apple': 1, 'mango': 1, 'potato': 1}}, {'NoFrills': {'mango': 1}}]
print("3", optimal_shipping(shipment_order_3, warehouses) == expected_output_3)

shipment_order_4 = {"apple": 1, "mango": 2, "cantaloupe": 4}
expected_output_4 = []
print("4", optimal_shipping(shipment_order_4, warehouses) == expected_output_4)

shipment_order_5 = {"apple": 0, "mango": 2, "potato": 1}
expected_output_5 = [{'FreshCo': {'mango': 1, 'potato': 1}}, {'NoFrills': {'mango': 1}}]
print("5", optimal_shipping(shipment_order_5, warehouses) == expected_output_5)

shipment_order_6 = {"apple": 7, "mango": 0}
expected_output_6 = [{'FreshCo': {'apple': 6}}, {'NoFrills': {'apple': 1}}]
print("6", optimal_shipping(shipment_order_6, warehouses) == expected_output_6)

shipment_order_7 = {"apple": 12, "mango": 1}
expected_output_7 = []
print("7", optimal_shipping(shipment_order_7, warehouses) == expected_output_7)
