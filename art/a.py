

def calculate_total(price, quantity):
    return price * quantity


def print_bill(item, price, quantity):
    total = calculate_total(price, quantity)

    print("\n--- Art Supplies Bill ---")
    print("Item:", item)
    print("Price: £", price)
    print("Quantity:", quantity)
    print("Total: £", total)


item = input("Enter the art supply: ")
price = float(input("Enter the price: £"))
quantity = int(input("Enter the quantity: "))

print_bill(item, price, quantity)