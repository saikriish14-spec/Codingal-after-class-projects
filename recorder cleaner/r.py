

students = {
    "Alice": ["Maths", "English", "Science", "Maths"],
    "Ben": ["History", "Maths", "Science"],
    "Charlie": ["English", "English", "Art"]
}


student = input("Enter a student name: ")

if student in students:
    print("Subjects:", students[student])
else:
    print("Student not found.")


students["David"] = ["Maths", "Computing", "Science"]

if "Alice" in students:
    students["Alice"].append("Computing")

for name in students:
    students[name] = list(set(students[name]))


students.pop("David", None)

print("\nNumber of student records:", len(students))


print("\nFinal Student Records:")

for name, subjects in students.items():
    print(name, ":", subjects)