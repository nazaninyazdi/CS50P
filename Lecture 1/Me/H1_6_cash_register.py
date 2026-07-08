product_name = input("Enter your product's name:  ")
product_price = float(input("Enter your product's price: "))
product_inventory = int(input("Enter your product's inventory: "))
total = product_inventory * product_price
if total >= 1000:
    discount = total * 0.1
    final = total - discount
    print(f"Product: {product_name}")
    print(f"Discount: {discount}")
    print(f"Final price: {final}")
else:
    print(f"Product: {product_name}")
    print(f"Price: {product_price}")
    print("No discount")
    print(f"Quantity: {product_inventory}")