from tkinter import *
from tkinter.font import Font
from tkinter import messagebox
from test import *
#globally expression declare variable--------------------------------
expression=""
#function for update expression-------------------------------------
def press(num):
    global expression
    expression=expression + str(num)
    equation.set(expression)
#function to evaluate final exoression------------------------------
def equalpress():
    try:
        global expression
        total=str(eval(expression))
        equation.set(total)
        expression=" "
    except:
        equation.set("error")
        expression=" "

#function to clear the number--------------------------------------
def clear():
    global expression
    expression=" "
    equation.set(" ")


window=Tk()
window.configure(background="black")
window.title("calculator")
window.geometry("300x250")

equation=StringVar()

# entry code----------------------------------------------------------
entry=Entry(window,textvariable=equation)
entry.grid(columnspan=4,ipadx=70,pady=10)

#button code------------------------------------------------------------

button=Button(window,text="1",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press(1))
button.grid(row=4,column=0)
button=Button(window,text="2",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press(2))
button.grid(row=4,column=1)
button=Button(window,text="3",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press(3))
button.grid(row=4,column=2)
button=Button(window,text="4",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press(4))
button.grid(row=4,column=3)
button=Button(window,text="5",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press(5))
button.grid(row=5,column=0)
button=Button(window,text="6",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press(6))
button.grid(row=5,column=1)
button=Button(window,text="7",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press(7))
button.grid(row=5,column=2)
button=Button(window,text="8",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press(8))
button.grid(row=5,column=3)
button=Button(window,text="9",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press(9))
button.grid(row=6,column=0)
button=Button(window,text="0",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press(0))
button.grid(row=6,column=1)
button=Button(window,text="/",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press("/"))
button.grid(row=6,column=2)
button=Button(window,text="*",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press("*"))
button.grid(row=6,column=3)
button=Button(window,text="+",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press("+"))
button.grid(row=7,column=0)
button=Button(window,text="-",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press("-"))
button.grid(row=7,column=1)
button=Button(window,text="%",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=lambda:press("%"))
button.grid(row=7,column=2)
button=Button(window,text="=",bg="deepskyblue",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=equalpress)
button.grid(row=7,column=3)
button=Button(window,text="clear",bg="orange",fg="black"
              ,width=5,height=1,padx=13,pady=3,command=clear)
button.grid(row=8,column=0)

window.mainloop()
