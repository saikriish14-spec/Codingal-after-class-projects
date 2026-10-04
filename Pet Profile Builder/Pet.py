class Pet:
    pet_breed = "German Shepherd"
    def __init__(self,age,name,favourite_food):
        self.age = age
        self.name = name
        self.favourite_food = favourite_food
Sai = Pet("45", "Sai", "Mutton Biriyani")

print(f"Sai' age is {Sai.age}")
print(f"Sai' name is {Sai.name}")
print(f"Sai' favourite food is {Sai.favourite_food}")

        