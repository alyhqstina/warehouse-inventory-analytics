import csv


products = ["Laptop", "Keyboard", "Mouse"]


stock = [150, 300, 80]
reorder_points = [200, 250, 100]


print("MULTI-PRODUCT REORDER REPORT")
print("----------------------------")


for i in range(3):
    if stock[i] <= reorder_points[i]:
        print(products[i], "- REPLENISHMENT REQUIRED")
    else:
        print(products[i], "-SUFFICIENT STOCK")


print("---------------------------")
print("REPLENISHMENT QUANTITY REPORT")


target_stock = [300, 400, 200]


for i in range(3):
    if stock[i] <= reorder_points[i]:
        order_quantity = target_stock[i] - stock[i]
        print(products[i], "- Order", order_quantity, "units")


unit_cost = [800, 25, 15]


print("--------------------------")
print("PURCHASING COST REPORT")


total_cost = 0


for i in range(3):
    if stock[i] <= reorder_points [i]:
        order_quantity = target_stock[i] - stock[i]
        purchase_cost = order_quantity * unit_cost[i]


        print(products[i], "- $", purchase_cost)
        total_cost += purchase_cost


print("TOTAL PURCHASING COST: $", total_cost)


with open("replenishment_report.csv", "w", newline="") as file:
    writer = csv.writer(file)


    writer.writerow([
        "Product",
        "Current Stock",
        "Reorder Point",
        "Order Quantity",
        "Purchasing Cost"
    ])

    for i in range(3):
        if stock[i] <= reorder_points[i]:
            order_quantity = target_stock[i] - stock[i]
            purchase_cost = order_quantity * unit_cost[i]


            writer.writerow([
                products[i],
                stock[i],
                reorder_points[i],
                order_quantity,
                purchase_cost
            ])


print("Replenishment report exported successfully!")

