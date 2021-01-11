import tkinter
from tkinter import *

win = tkinter.Tk()
win.title("Calculator By Anish Nirala")
win.geometry("400x400+250+250")
win.configure(background="#9966ff")
# win.resizable(0, 0) # To prevent window from resizing

val = ""

def button1_clicked():
    global val
    val+="1"
    data.set(val)

def button2_clicked():
    global val
    val+="2"
    data.set(val)

def button3_clicked():
    global val
    val+="3"
    data.set(val)

def button_plus_clicked():
    global val
    val+="+"
    data.set(val)

def button4_clicked():
    global val
    val+="4"
    data.set(val)

def button5_clicked():
    global val
    val+="5"
    data.set(val)

def button6_clicked():
    global val
    val+="6"
    data.set(val)

def button_minus_clicked():
    global val
    val+="-"
    data.set(val)

def button7_clicked():
    global val
    val+="7"
    data.set(val)

def button8_clicked():
    global val
    val+="8"
    data.set(val)

def button9_clicked():
    global val
    val+="9"
    data.set(val)

def button_mul_clicked():
    global val
    val+="*"
    data.set(val)

def button_clear_clicked():
    global val
    val=""
    data.set(val)

def button0_clicked():
    global val
    val+="0"
    data.set(val)

def button_equal_clicked():
    global val
    valueList = []
    res = 0
    num = ""
    for k in range(len(val)):
        if(val[k] not in ['+','-','*','/']):
            num+=val[k]
        else:
            valueList.append(int(num))
            valueList.append(val[k])
            num=""
    valueList.append(int(num))
    print(valueList)
    while(len(valueList)>=3):
        val1, op, val2 = valueList[0], valueList[1], valueList[2]
        if(op=="/"):
            res = round(val1/val2, 4)
        elif(op=="*"):
            res = val1*val2
        elif(op=="+"):
            res = val1+val2
        elif(op=="-"):
            res = val1-val2
        valueList.pop(0)
        valueList.pop(0)
        valueList[0] = res
        print(valueList, res)
    data.set(val+"="+str(round(valueList[0],2)))
    val=""

def button_div_clicked():
    global val
    val+="/"
    data.set(val)


data = StringVar()
label = Label(
    win,
    text="Label",
    anchor=SE,
    font = ("Verdana", 20),
    textvariable = data,
    bg="#ffffff",
    fg="#000000",
)
label.pack(expand=True, fill="both")

frame1 = Frame(win)
frame1.pack(expand=True, fill="both")

frame2 = Frame(win)
frame2.pack(expand=True, fill="both")

frame3 = Frame(win)
frame3.pack(expand=True, fill="both")

frame4 = Frame(win)
frame4.pack(expand=True, fill="both")

btn1 = Button(
    frame1,
    text="1",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button1_clicked,
)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(
    frame1,
    text="2",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button2_clicked,
)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(
    frame1,
    text="3",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button3_clicked,
)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(
    frame1,
    text="+",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button_plus_clicked,
)
btn4.pack(side=LEFT, expand=True, fill="both")

btn5 = Button(
    frame2,
    text="4",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button4_clicked,
)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(
    frame2,
    text="5",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button5_clicked,
)
btn6.pack(side=LEFT, expand=True, fill="both")

btn7 = Button(
    frame2,
    text="6",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button6_clicked,
)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(
    frame2,
    text="-",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button_minus_clicked,
)
btn8.pack(side=LEFT, expand=True, fill="both")

btn9 = Button(
    frame3,
    text="7",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button7_clicked,
)
btn9.pack(side=LEFT, expand=True, fill="both")

btn10 = Button(
    frame3,
    text="8",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button8_clicked,
)
btn10.pack(side=LEFT, expand=True, fill="both")

btn11 = Button(
    frame3,
    text="9",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button9_clicked,
)
btn11.pack(side=LEFT, expand=True, fill="both")

btn12 = Button(
    frame3,
    text="*",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button_mul_clicked,
)
btn12.pack(side=LEFT, expand=True, fill="both")

btn13 = Button(
    frame4,
    text="C",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button_clear_clicked,
)
btn13.pack(side=LEFT, expand=True, fill="both")

btn14 = Button(
    frame4,
    text="0",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button0_clicked,
)
btn14.pack(side=LEFT, expand=True, fill="both")

btn15 = Button(
    frame4,
    text="=",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button_equal_clicked,
)
btn15.pack(side=LEFT, expand=True, fill="both")

btn16 = Button(
    frame4,
    text="/",
    font=("Verdana", 22),
    relief=GROOVE,
    border=0,
    command = button_div_clicked,
)
btn16.pack(side=LEFT, expand=True, fill="both")

win.mainloop()