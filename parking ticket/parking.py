

PRICE = 5.00
VALID_COINS = [0.10, 0.20, 0.50, 1.00, 2.00]

def get_change(amount):
    return amount - PRICE

paid = 0.0

print("Parking Ticket Payment Helper")
print("Ticket price: £5.00")
print("Valid coins: 10p, 20p, 50p, £1, £2")

while paid < PRICE:
    coin = float(input("Insert a coin: £"))


    if coin not in VALID_COINS:
        print("Invalid coin. Try again.")
        continue

    paid += coin
    print("Total paid: £", round(paid, 2))

  
    if paid >= PRICE:
        break

change = get_change(paid)

if change > 0:
    print("Your change is: £", round(change, 2))
elif change == 0:
    print("No change needed.")
else:
    pass

print("Payment complete. Thank you!")