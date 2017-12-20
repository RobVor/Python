import tkinter

mainWindow = tkinter.Tk()

def CalcMiles():
    print("We are counting the miles!")
    lblText.delete('1.0',tkinter.END)
    print(txtInputVar.get())
    Miles = float(txtInputVar.get()) * 1.6
    lblText.insert(tkinter.END, Miles)

def RetryCalc():
    print("Clearing the input")
    txtInput.delete(0,tkinter.END)
    lblText.delete("1.0", tkinter.END)
    print("Moving to...")
    txtInput.focus()

btnFirst = tkinter.Button(mainWindow, text="First Button", command=CalcMiles)
#btnFirst.pack() # Pack builds the objects but... Grid might be better for position control
btnFirst.grid(row=0,column=0,rowspan=1,columnspan=1)

btnSecond = tkinter.Button(mainWindow, text="Try another", command=RetryCalc)
btnSecond.grid(row=0, column=1,rowspan=1,columnspan=1)

txtInputVar = tkinter.StringVar()
txtInput = tkinter.Entry(mainWindow, textvariable=txtInputVar,width=12,text=0)
txtInput.grid(row=1, column=0,rowspan=1,columnspan=1)

lblText = tkinter.Text(mainWindow,height=1,width=20)
lblText.grid(row=1,column=1,rowspan=3,columnspan=1)

mainWindow.columnconfigure(0,weight=1)
mainWindow.columnconfigure(1,weight=1)
mainWindow.mainloop()