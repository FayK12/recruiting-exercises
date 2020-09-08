#function to iterate through shipping list at a warehouse
def warehouse_purchase(shipment_order, warehouse_inventory, purchased, clear_shipment_order):
  
  for fruit in shipment_order:
    #add name of item to be removed which has '0' quantity to begin with
    if shipment_order[fruit] == 0:
      clear_shipment_order.add(fruit)

    #buy the necessary items that are in shipping list and available in warehouse
    #buy the quantity you need and update the shipping list accordingly
    if fruit in shipment_order and fruit in warehouse_inventory and warehouse_inventory[fruit] > 0 and shipment_order[fruit] > 0:
      available = warehouse_inventory[fruit]

      #when you need more items than what's available at warehouse
      if (shipment_order[fruit] > available):
          shipment_order[fruit] -= available
          purchased[fruit] = available
      #when warehouse has more items than what you need
      else:
        purchased[fruit] = shipment_order[fruit]
        shipment_order[fruit] = 0
        clear_shipment_order.add(fruit)
        
  return shipment_order, purchased, clear_shipment_order


def optimal_shipping(shipment_order, warehouses):

    checkout = []

    #edge case for empty shipping list
    if len(shipment_order) == 0:
      return checkout

    #iterate through all warehouses
    for i in range(len(warehouses)):
      
      name = warehouses[i]['name']
      warehouse_inventory = warehouses[i]['inventory']
      #collects items purchased at a store
      purchased = {}
      #collects key:value pairs of warehouse:items purchased
      warehouse_items = {}
      #set is used to store items with '0' quantity and then iterate the shipping list to remove them
      clear_shipment_order = set()
      
      #iterate in warehouses which have items and when shipping list has items too
      if len(warehouse_inventory) > 0 and len(shipment_order) > 0:
        #helper function returning updated shipping list, items purchased at a warehouse, and set of items to be removed
        #from shipping list
        shipment_order, purchased, clear_shipment_order = warehouse_purchase(shipment_order, warehouse_inventory, purchased, clear_shipment_order)
        
        if len(clear_shipment_order) > 0:
          #remove each item that's in the set from the shipping list
          for fruit in clear_shipment_order:
            del shipment_order[fruit]

        #add warehouse and the list of items purchased from there into another dictionary, warehouse_items
        #add the dictionary to the checkout list
        if len(purchased) > 0:
          warehouse_items[name] = purchased
          checkout.append(warehouse_items)
    
    #if there are still items left in shipping list, there were none found in warehouses      
    if len(shipment_order) > 0:
      checkout = []

    return checkout

      
warehouses = [{
        "name": "owd",
        "inventory": {
            "apple": 6,
            "mango": 1,
            "potato": 1
    }
    }, 
    {
        "name": "oz",
        "inventory": {}
    },
    {
        "name": "dm",
        "inventory": {
            "apple": 5,
            "mango": 1
    }
    }]

"""
shipment_order_0 = {}
expected_output_0 = []
print("0", optimal_shipping(shipment_order_0, warehouses) == expected_output_0)

shipment_order_1 = {"apple": 1}
expected_output_1 = [{'owd': {'apple': 1}}]
print("1",optimal_shipping(shipment_order_1, warehouses) == expected_output_1)

shipment_order_2 = {"apple": 1, "mango": 1, "potato": 1}
expected_output_2 = [{'owd': {'apple': 1, 'mango': 1, 'potato': 1}}]
print("2", optimal_shipping(shipment_order_2, warehouses) == expected_output_2)

shipment_order_3 = {"apple": 1, "mango": 2, "potato": 1}
expected_output_3 = [{'owd': {'apple': 1, 'mango': 1, 'potato': 1}}, {'dm': {'mango': 1}}]
print("3", optimal_shipping(shipment_order_3, warehouses) == expected_output_3)

shipment_order_4 = {"apple": 1, "mango": 2, "cantaloupe": 4}
expected_output_4 = []
print("4", optimal_shipping(shipment_order_4, warehouses) == expected_output_4)

shipment_order_5 = {"apple": 0, "mango": 2, "potato": 1}
expected_output_5 = [{'owd': {'mango': 1, 'potato': 1}}, {'dm': {'mango': 1}}]
print("5", optimal_shipping(shipment_order_5, warehouses) == expected_output_5)

shipment_order_7 = {"apple": 12, "mango": 1}
expected_output_7 = []
print("7", optimal_shipping(shipment_order_7, warehouses) == expected_output_7)

shipment_order_8 = {"apple": 7, "mango": 0}
expected_output_8 = [{'owd': {'apple': 6}}, {'dm': {'apple': 1}}]
print("8", optimal_shipping(shipment_order_8, warehouses) == expected_output_8)"""
