import tkinter as tk

count = 0

def increase_count():
    global count
    count = count + 1
    label.config(text="Clicks: " + str(count))

window = tk.Tk()
window.title("Click Counter")
window.geometry("300x200")

label = tk.Label(window, text="Clicks: 0", font=("Google Sans", 20))
label.pack(pady=20)

button = tk.Button(window, text="Click me!", command=increase_count)
button.pack()

window.mainloop()
