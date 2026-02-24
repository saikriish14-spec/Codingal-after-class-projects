# Ask the user for the temperature

# use conditional statements to decide which clothes to wear 

temperature = float(input("Enter the temperature  : "))

if temperature >= 25:
    print("It's warm You can wear light clothes.")
elif 15 <= temperature < 25:
    print("It's mild wear a light jacket.")
else:
    print("It's cold wear warm clothes")



