import csv


products = ["Laptop", "Keyboard", "Mouse", "Monitor", "Printer"]
stock = [150, 300, 500, 80, 40]
unit_cost = [800, 25, 15, 200, 350]


target_stock = 100


with open("inventory_report.csv", "w", newline="") as file:
    writer = csv.writer(file)


    writer.writerow(["Product", "Stock", "Unit Cost",
                    "Stock Status", "Replenishment Qty"])


    for i in range(5):
        if stock[i] < target_stock:
            status = "LOW STOCK"
            shortage = target_stock - stock[i]
        else:
            status = "SUFFICIENT STOCK"
            shortage = 0


        writer.writerow([products[i], stock[i],
                         unit_cost[i], status, shortage])


print("Inventory report exported successfully!")
