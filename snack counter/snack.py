
box1 = {"apple", "banana", "crisps", "chocolate"}
box2 = {"banana", "crisps", "juice", "sandwich"}

print("Box 1:", box1)
print("Box 2:", box2)

box1.add("cookie")
print("Box 1 after adding a snack:", box1)

shared_snacks = box1.intersection(box2)
print("Shared snacks:", shared_snacks)

snacks = ["apple", "banana", "crisps", "chocolate", "juice"]

print("Snack array:", snacks)

snacks.append("cookie")
print("After adding a snack:", snacks)


snacks.remove("banana")
print("After removing a snack:", snacks)

snacks.append("apple")
apple_count = snacks.count("apple")
print("Number of apples:", apple_count)

snacks.reverse()
print("Reversed snack array:", snacks)

print("\nFinal Snack Counter:")
print(snacks)