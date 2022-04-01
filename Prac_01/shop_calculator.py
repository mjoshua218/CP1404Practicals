number_of_items = int(input("Number of Items: "))
total = 0

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of Items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: $"))
    total += price_of_item
if total > 100:
    total = total * 0.9
print(f"total price for {number_of_items} items is {total:.2f}$")