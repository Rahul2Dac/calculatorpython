from tkinter import *

window = Tk()
window.title("CALCULATOR")
display = Entry(window, width=35,borderwidth=5)
display.grid(row=0,column=0, columnspan=4, padx=5, pady=20)


# display.insert(0,"enter the number")#display

def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def button_multiply():
    first_number = display.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    display.delete(0, END)
def button_division():
    first_number = display.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    display.delete(0, END)
def button_subtract():
    first_number = display.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    display.delete(0, END)

def button_equal():
    second_number = display.get()
    display.delete(0, END)
    if math == "addition":
        display.insert(0, f_num + int(second_number))
    if math == "multiplication":
        display.insert(0, f_num * int(second_number))
    if math == "subtract":
        display.insert(0, f_num - int(second_number))
    if math == "division":
        display.insert(0, f_num / int(second_number))


button_1 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_click(1), text="1",
                  font=("Courier New", 16, 'bold'))
button_2 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_click(2), text="2",
                  font=("Courier New", 16, 'bold'))
button_3 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_click(3), text="3",
                  font=("Courier New", 16, 'bold'))
button_4 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_click(4), text="4",
                  font=("Courier New", 16, 'bold'))
button_5 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_click(5), text="5",
                  font=("Courier New", 16, 'bold'))
button_6 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_click(6), text="6",
                  font=("Courier New", 16, 'bold'))
button_7 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_click(7), text="7",
                  font=("Courier New", 16, 'bold'))
button_8 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_click(8), text="8",
                  font=("Courier New", 16, 'bold'))
button_9 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_click(9), text="9",
                  font=("Courier New", 16, 'bold'))
button_0 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_click(0), text="0",
                  font=("Courier New", 16, 'bold'))

button_division1= Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_division(), text="/",
                    font=("Courier New", 16, 'bold'))
button_multiplication = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_multiply(), text="x",
                    font=("Courier New", 16, 'bold'))
button_subtract1 = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda: button_subtract(), text="-",
                    font=("Courier New", 16, 'bold'))
button_poi = Button(window, padx=35, pady=0, bd=4, bg='white', command=lambda: button_click(), text=".",
                    font=("Courier New", 16, 'bold'))
# button_eql=Button(window,padx=35,pady=0,bd=4,bg='white',command=button_add(),text="=",font=("Courier New",16,'bold'))


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

button_division1.grid(row=1,column=3)
button_multiplication.grid(row=2, column=3)
button_subtract1.grid(row=3, column=3)
button_poi.grid(row=4, column=1, columnspan=2)


# buttonql.grid(row=4, column=1,columnspan=2)

button_addition = Button(window, padx=5, pady=0, bd=4, bg='white', command=lambda:button_add(), text="+",
                    font=("Courier New", 16, 'bold'))

button_addition.grid(row=4, column=3)



def button_clear():
    display.delete(0, END)

button_clr = Button(window, padx=34.2, pady=0, bd=4, bg='white', command=lambda: button_clear(), text="C",
                    font=("Courier New", 16, 'bold'))
button_clr.grid(row=5, column=0, columnspan=2)
button_eql = Button(window, padx=34.2, pady=0, bd=4, bg='white', command=lambda: button_equal(), text="=",
                    font=("Courier New", 16, 'bold'))
button_eql.grid(row=5, column=2, columnspan=2)

def button_add():
    first_number = display.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    display.delete(0, END)



window.mainloop()









