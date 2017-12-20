import tkinter

mainWindow = tkinter.Tk()
btnFirst = tkinter.Button(mainWindow, text="First Button")
btnFirst.pack()
text=tkinter.Text(mainWindow)
text.pack(side="left",fill="both",expand="YES")

def ButtonPressed(event):
    print("Pressed", repr(event.keysym))

def KeyTest(a):
    print("Test seems to have worked, pressed %s: control key %s" %(repr(event.keysym),str(a)))

for i in range(1,5):
    text.bind("<Control-Key-"+str(i)+">",ButtonPressed)

mainWindow.mainloop()