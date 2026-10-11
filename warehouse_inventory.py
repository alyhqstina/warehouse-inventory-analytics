# Warehouse Inventory Management
# Project 1 - Supply Chain Analytics


products = ["Laptop", "Keyboard", "Mouse", "Monitor", "Printer"]
stock = [150, 300, 500, 80, 40]

reorder_level = 100


print("WAREHOUSE INVENTORY REPORT")
print("--------------------------")


for i in range(5):
    if stock[i] < reorder_level:
        print(products[i], "- LOW STOCK")
    else:
        print(products[i], "- SUFFICIENT STOCK")

print("--------------------------")
print("REPLENISHMENT REPORT")


for i in range(5):
    if stock[i] < reorder_level:
        shortage = reorder_level - stock[i]
        print(products[i], "- Replenish", shortage, "units")

unit_cost = [800, 25, 15, 200, 350]


print("-------------------------")
print("PURCHASING COST REPORT")


total_cost = 0


for i in range(5):
    if stock[i] < reorder_level:
        shortage = reorder_level - stock[i]
        purchase_cost = shortage * unit_cost[i]


        print(products[i], "- $", purchase_cost)


        total_cost = total_cost + purchase_cost


print(f"TOTAL PURCHASING COST: ${total_cost:,.2f}")
