import random
import math

print(" Random Fun Calculator ")


lucky_number = random.randint(1, 100)
print("Your lucky number is:", lucky_number)

activities = ["Play cricket", "Play games", "Watch a movie", "Go outside", "Listen to music"]
activity = random.choice(activities)
print("Your random activity is:", activity)

secret_number = random.randint(1, 10)

guess = int(input("Guess a number from 1 to 10: "))

if guess == secret_number:
    print("Correct! You guessed it!")
else:
    print("Wrong! The number was", secret_number)
number = float(input("Enter a number: "))

print("Ceiling:", math.ceil(number))
print("Floor:", math.floor(number))
print("Absolute value:", math.fabs(number))
print("Cosine:", math.cos(number))
print("GCD of 12 and 8:", math.gcd(12, 8))

x = float(input("Enter a number for copysign: "))
y = float(input("Enter another number: "))

print("Copysign result:", math.copysign(x, y))

print("Thanks for using the Random Fun Calculator!")