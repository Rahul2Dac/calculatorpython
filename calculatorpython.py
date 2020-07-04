from tkinter import *

window = Tk()
window.title("CALCULATOR")
display = Entry(window, width=35, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=5, pady=10)


# display.insert(0,"enter the number")#display

def button_add():
    return

button_1=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="1",font=("Courier New",16,'bold'))
button_2=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="2",font=("Courier New",16,'bold'))
button_3=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="3",font=("Courier New",16,'bold'))
button_4=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="4",font=("Courier New",16,'bold'))
button_5=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="5",font=("Courier New",16,'bold'))
button_6=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="6",font=("Courier New",16,'bold'))
button_7=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="7",font=("Courier New",16,'bold'))
button_8=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="8",font=("Courier New",16,'bold'))
button_9=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="9",font=("Courier New",16,'bold'))
button_0=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="0",font=("Courier New",16,'bold'))

button_div=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="/",font=("Courier New",16,'bold'))
button_mul=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="*",font=("Courier New",16,'bold'))
button_sub=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="-",font=("Courier New",16,'bold'))
button_eql=Button(window,padx=35,pady=0,bd=4,bg='white',command=button_add(),text="=",font=("Courier New",16,'bold'))
#button_eql=Button(window,padx=35,pady=0,bd=4,bg='white',command=button_add(),text="=",font=("Courier New",16,'bold'))


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_div.grid(row=1, column=3)
button_mul.grid(row=2, column=3)
button_sub.grid(row=3, column=3)
button_eql.grid(row=4, column=1,columnspan=2)
#button_eql.grid(row=4, column=1,columnspan=2)

def button_add():
   return

button_add=Button(window,padx=5,pady=0,bd=4,bg='white',command=button_add(),text="+",font=("Courier New",16,'bold'))
button_add.grid(row=4, column=3)

window.mainloop()
