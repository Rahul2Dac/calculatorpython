from tkinter import *
window = Tk()
window.title ("CALCULATOR")
display = Entry (window,width = 35,borderwidth = 5)
display.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
display.insert(0,"enter the number")
window.mainloop()
