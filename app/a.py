# Student App Access Manager

# Approved and restricted apps
approved_apps = {"Calculator", "Notes", "School", "Teams"}
restricted_apps = {"YouTube", "TikTok", "Games"}

# Ask for student details
name = input("Enter your name: ")
age = input("Enter your age: ")

# Check data types
print("\nData Type Check:")
print("Name is a string:", isinstance(name, str))
print("Age is a string:", isinstance(age, str))

age = int(age)

print("Age is an integer:", isinstance(age, int))

# Ask for an app
app = input("\nEnter the app you want to access: ")

# Check app lists
if app in approved_apps:
    print("This app is approved.")
elif app in restricted_apps:
    print("This app is restricted.")
else:
    print("This app is not on the list.")

# Binary permissions
READ = 1      # 001
WRITE = 2     # 010
EXECUTE = 4   # 100

student_permissions = READ | WRITE

print("\nPermissions:")
print("Binary permissions:", bin(student_permissions))

# Bitwise AND to check permissions
if student_permissions & READ:
    print("Read permission: Allowed")
else:
    print("Read permission: Not allowed")

if student_permissions & WRITE:
    print("Write permission: Allowed")
else:
    print("Write permission: Not allowed")

if student_permissions & EXECUTE:
    print("Execute permission: Allowed")
else:
    print("Execute permission: Not allowed")

# Bitwise OR to add execute permission
student_permissions = student_permissions | EXECUTE

print("\nAfter adding execute permission:")
print("Permissions:", bin(student_permissions))

# Bit shifts
left_shift = student_permissions << 1
right_shift = student_permissions >> 1

print("Left shift:", left_shift)
print("Right shift:", right_shift)

print("\nAccess check complete for", name)