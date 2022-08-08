total = 0
item = int(input("Number of items: "))
while item < 0:
    print("Invalid number of items!")
for i in range(item):
    price_of_item = float(input("Price of item: "))
    total += price_of_item
if total >= 100:
    total *= 0.9
print("Total price for ", item, "items is $ ", total)