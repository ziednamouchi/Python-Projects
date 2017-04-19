from tkinter import *
from tkinter import ttk



# ---------- TKINTER EVENTS  ----------

def get_sum(event):
    # Get the value stored in the entries
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum = num1 + num2

    # Delete the value in the entry
    sumEntry.delete(0, "end")

    # Insert the sum into the entry
    sumEntry.insert(0, sum)


root = Tk()

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text="+").pack(side=LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text="=")

# When the left mouse button is clicked call the
# function get_sum
equalButton.bind("<Button-1>", get_sum)

equalButton.pack(side=LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)

root.mainloop()
