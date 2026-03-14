base = int(input("Enter a number "))
power = int(input("enter a power"))

result = 1 
for i in range(power):
    result = result * base
    print("result:", result)