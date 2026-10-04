books = ["Python Basics", "Data Structures", "Web Design", "AI Handbook"]
copies = [3, 0, 2, 0]
fees = [1.50, 2.00, 0.75, 3.00]


pairs = list(zip(books, copies))


available = list(filter(lambda p: p[1] > 0, pairs))
print("Available:", available)


new_fees = list(map(lambda f: round(f * 1.1, 2), fees))


for name, count, fee in zip(books, copies, new_fees):
    print(name, count, fee)


chosen = input("Choose a book: ")
for name, count in pairs:
    if name == chosen:
        if count == 0:
            print("Sorry, that book is unavailable.")
            break
        print("Enjoy your book!")
        break