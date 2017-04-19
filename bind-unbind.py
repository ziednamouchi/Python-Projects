from tkinter import *


def get_data(event):
    # Output the values for the Widgets with get()
    print("String :", strVar.get())
    print("Integer :", intVar.get())
    print("Double :", dblVar.get())
    print("Boolean :", boolVar.get())

# You can unbind and rebind an event to a function
def bind_button(event):
    if boolVar.get():
        button1.unbind("<Button-1>")
    else:
        button1.bind("<Button-1>", get_data)


root = Tk()

# there are TkInter variables
# you can use with Widgets to set and get values
strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

# Set the default values with set()
strVar.set("Enter String")
intVar.set("Enter Integer")
dblVar.set("Enter Double")
boolVar.set(True)

# Assign the variable to either textvariable or variable
strEntry = Entry(root, textvariable=strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable=intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable=dblVar)
dblEntry.pack(side=LEFT)

# Depending on if this check button is selected or not
# will determine if we can get data on our Widgets
theCheckBut = Checkbutton(root, text="Switch", variable=boolVar)
theCheckBut.bind("<Button-1>", bind_button)
theCheckBut.pack(side=LEFT)


button1 = Button(root, text="Get Data")
button1.bind("<Button-1>", get_data)
button1.pack(side=LEFT)

root.mainloop()
