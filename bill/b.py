

def calculate_bill(food, drinks, dessert):
    """Calculate the total restaurant bill using positional arguments."""
    return food + drinks + dessert


def seating_arrangements(people):
    """Calculate seating arrangements recursively."""
    if people <= 1:
        return 1
    return people * seating_arrangements(people - 1)



food = 25
drinks = 10
dessert = 8

total_bill = calculate_bill(food, drinks, dessert)

print("Restaurant Bill")
print("Food: £", food)
print("Drinks: £", drinks)
print("Dessert: £", dessert)
print("Total: £", total_bill)

print("\nFunction description:")
print(calculate_bill.__doc__)

people = int(input("\nHow many people are sitting at the table? "))

arrangements = seating_arrangements(people)

print("Number of seating arrangements:", arrangements)