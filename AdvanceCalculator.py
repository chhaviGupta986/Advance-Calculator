import tkinter
import math
from tkinter.constants import END

calci = tkinter.Tk()
calci.title("Advance Calculator")
calci.minsize(width=650,height=420)
calci.config(bg="black")
entrybox=tkinter.Entry(calci,width=49,bd=10,font=("Arabic",18),bg="white",fg="magenta")
entrybox.grid(row=0,column=0,columnspan=8)

def click(value):
    box = entrybox.get()
    answer = ""
    try:
        if value == "C":
            box = entrybox.get()
            box = box[0:len(box)-1]
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, box)
        elif value == "CE":
            entrybox.delete(0, len(box)+1)
        elif value == "√":
            answer = math.sqrt(eval(box))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "cos":
            answer = math.cos(math.radians(eval(box)))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "sin":
            answer = math.sin(math.radians(eval(box)))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "tan":
            answer = math.tan(math.radians(eval(box)))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "cosh":
            answer = math.cosh(math.radians(eval(box)))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "sinh":
            answer = math.sinh(math.radians(eval(box)))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "tanh":
            answer = math.tanh(math.radians(eval(box)))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "π":
            answer = math.pi
            entrybox.insert(END, answer)
        elif value == "2π":
            answer = (math.pi)*2
            entrybox.insert(END, answer)
        elif value == chr(8731):
            answer = eval(box)**(1/3)
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == chr(247):
            entrybox.insert(END, "/")
        elif value == "^":
            entrybox.insert(END, "**")
        elif value == "x\u00B3":
            entrybox.insert(END, "**3")
        elif value == "x\u00B2":
            entrybox.insert(END, "**2")
        elif value == "ln":
            answer = math.log2(eval(box))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "deg":
            answer = math.degrees(eval(box))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "rad":
            answer = math.radians(eval(box))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "x!":
            answer = math.factorial(eval(box))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "e":
            answer = math.e
            entrybox.insert(0, answer)
        elif value == "log10":
            answer = math.log10(eval(box))
            entrybox.delete(0, len(box)+1)
            entrybox.insert(0, answer)
        elif value == "=":
            answer = eval(box)
            entrybox.delete(0, len(box))
            entrybox.insert(0, answer)
            print(answer)
        else:
            entrybox.insert(len(box), value)

    except SyntaxError:
        entrybox.delete(0, len(box))
        entrybox.insert(0, "Syntax Error")

    except:
        entrybox.delete(0, len(box))        


lst = ["C","CE","√","+","π","cos","tan","sin","1","2","3","-","2π", "cosh", "tanh", "sinh", "4", "5", "6", "*",
       chr(8731), "^", "x\u00B3", "x\u00B2", "7", "8", "9", chr(247), "ln", "deg", "rad", "e", "0", ".", "%", "=", "log10", "(", ")", "x!"]
rowval = 1
colval = 0
for i in (lst):
    button = tkinter.Button(calci, width=5, height=2, text=i, bd=2, fg="white", font=(
        "Arabic", 18), bg="black", command=lambda button=i: click(button))
    button.grid(row=rowval, column=colval)
    colval += 1
    if colval > 7:
        rowval += 1
        colval = 0

calci.mainloop()
