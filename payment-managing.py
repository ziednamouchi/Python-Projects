import time
import datetime
from tkinter import *


root = Tk()

root.title("Payroll system")
root.geometry("1350x650+0+0")

#===========================================Frames=================================================
Tops = Frame(root, width=1350, height=50, bd=8, relief="raise")
Tops.pack(side=TOP)

f1 = Frame(root, width=600, height=600, bd=8, relief="raise")
f1.pack(side=LEFT)

f2 = Frame(root, width=300, height=600, bd=8, relief="raise")
f2.pack(side=RIGHT)

f1a= Frame(f1, width=600, height=200, bd=20, relief="raise")
f1a.pack(side=TOP)

f1b = Frame(f1, width=600, height=600, bd=20, relief="raise")
f1b.pack(side=TOP)

#===========================================Labels=================================================
lblinfo = Label(Tops, font=("arial ", 68, "bold"), bd=10, text="Payment Management System")
lblinfo.grid(row=0, column=0)

lblName = Label(f1a, text="Name", font=("arial", 16, "bold"), bd=20).grid(row=0, column=0)
lblAddress = Label(f1a, text="Address", font=("arial", 16, "bold"), bd=20).grid(row=0, column=2)

lblEmployer = Label(f1a, text="Employer", font=("arial", 16, "bold"), bd=20).grid(row=1, column=0)
lblNINumber = Label(f1a, text="NI Number", font=("arial", 16, "bold"), bd=20).grid(row=1, column=2)

lblHoursWorked = Label(f1a, text="Hours Worked", font=("arial", 16, "bold"), bd=20).grid(row=2, column=0)
lblHourlyRate = Label(f1a, text="Hourly Rate", font=("arial", 16, "bold"), bd=20).grid(row=2, column=2)

lblTaxe = Label(f1a, text="Taxes", font=("arial", 16, "bold"), bd=20).grid(row=3, column=0)
lblOvertime = Label(f1a, text="Overtime", font=("arial", 16, "bold"), bd=20).grid(row=3, column=2)

lblGrossPay = Label(f1a, text="Gross Pay", font=("arial", 16, "bold"), bd=20).grid(row=4, column=0)
lblNetPay = Label(f1a, text="Net Pay", font=("arial", 16, "bold"), bd=20).grid(row=4, column=2)

#===========================================Variables=================================================
Name = StringVar()
Address = StringVar()
Employer = StringVar()
NINumber = StringVar()
HoursWorked = StringVar()
WagesHour = StringVar()
Payable = StringVar()
Taxable = StringVar()
NetPayable = StringVar()
GrossPayable = StringVar()
OvertimeHours = StringVar()
TimeOfOrder = StringVar()
DateOfOrder = StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

#===========================================Entries=================================================
etxtName = Entry(f1a, textvariable=Name, font=("arial", 16, "bold"), bd=16, justify='left', width=22)
etxtName.grid(row=0, column=1)

etxtAddress = Entry(f1a, textvariable=Address, font=("arial", 16, "bold"), bd=16, justify='left', width=22)
etxtAddress.grid(row=0, column=3)

etxtEmployer = Entry(f1a, textvariable=Employer, font=("arial", 16, "bold"), bd=16, justify='left', width=22)
etxtEmployer.grid(row=1, column=1)

etxtNINumber = Entry(f1a, textvariable=NINumber, font=("arial", 16, "bold"), bd=16, justify='left', width=22)
etxtNINumber.grid(row=1, column=3)

etxtHoursWorked = Entry(f1a, textvariable=HoursWorked, font=("arial", 16, "bold"), bd=16, justify='left', width=22)
etxtHoursWorked.grid(row=2, column=1)

etxtHourlyRate = Entry(f1a, textvariable=WagesHour, font=("arial", 16, "bold"), bd=16, justify='left', width=22)
etxtHourlyRate.grid(row=2, column=3)

etxtTax = Entry(f1a, textvariable=Taxable, font=("arial", 16, "bold"), bd=16, justify='left', width=22)
etxtTax.grid(row=3, column=1)

etxtOvertime = Entry(f1a, textvariable=OvertimeHours, font=("arial", 16, "bold"), bd=16, justify='left', width=22)
etxtOvertime.grid(row=3, column=3)

etxtGrossPay = Entry(f1a, textvariable=Payable, font=("arial", 16, "bold"), bd=16, justify='left', width=22)
etxtGrossPay.grid(row=4, column=1)

etxtNetPay = Entry(f1a, textvariable=NetPayable, font=("arial", 16, "bold"), bd=16, justify='left', width=22)
etxtNetPay.grid(row=4, column=3)

#===========================================Text=================================================
lblPaySlip = Label(f2, font=("arial", 20, "bold"), textvariable=DateOfOrder).grid(row=0, column=0)
txtPaySlip = Text(f2, height=22, width=34, bd=16, font=("arial", 12, "bold"))
txtPaySlip.grid(row=1, column=0)

root.mainloop()
