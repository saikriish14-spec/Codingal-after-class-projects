
marks = [78, 85, 92, 67, 88]


print("Student Marks:", marks)


print("Number of marks:", len(marks))


print("First mark:", marks[0])
print("Last mark:", marks[-1])

print("Last two marks:", marks[-2:])


print("\nAll Marks:")
for mark in marks:
    print(mark)


total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)


print("\nSummary")
print("Total:", total)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)