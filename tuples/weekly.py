
habit = ("Exercise", "30 minutes", "Daily")


week = ("Mon ✔", "Tue ✔", "Wed ✘", "Thu ✔", "Fri ✔", "Sat ✘", "Sun ✔")
print("Weekly Record:", week)


print("Number of days:", len(week))


print("First day:", week[0])
print("Last day:", week[-1])


print("Weekdays:", week[:5])
print("Weekend:", week[5:])

try:
    week[0] = "Mon ✘"
except TypeError:
    print("Tuples cannot be changed because they are immutable.")