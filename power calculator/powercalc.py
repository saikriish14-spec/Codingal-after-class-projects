base = int(input("Enter the base number :"))
exponent = int(input("Enter the exponent number :"))
result = 1

for i in range(1, exponent + 1):
    result *= base
print(result)

print("Answer:", base, "to the power", exponent, "=", result)