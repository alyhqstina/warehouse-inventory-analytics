daily_demand = 30
lead_time = 5
safety_stock = 50


reorder_point = (daily_demand * lead_time) + safety_stock


print("REORDER POINT REPORT")
print("--------------------")
print("Reorder Point:", reorder_point, "units")


daily_demand = 30
lead_time = 8
safety_stock = 50


reorder_point = (daily_demand * lead_time) + safety_stock


print("REORDER POINT REPORT")
print("--------------------")
print("Reorder Point:", reorder_point, "units")



current_stock = 250


if current_stock <= reorder_point:
    print("REPLENISHMENT REQUIRED")
else:
    print("STOCK LEVEL SUFFICIENT")


target_stock = 400


if current_stock <= reorder_point:
    order_quantity = target_stock - current_stock
    print("Order Quantity:", order_quantity, "units")
else:
    print("No replenishment needed")


unit_cost = 35


purchase_cost = order_quantity * unit_cost


print("PURCHASING COST REPORT")
print("Order Quantity:", order_quantity, "units")
print("Total Purchasing Cost: $", purchase_cost)
