from tkinter import *
root=Tk()

def click(event):
    global scvalue

    text=event.widget.cget("text")
    print(text)

    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(scvalue.get())
            except Exception as e:
                print(e)
                value="Error"
        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root.geometry("600x600")
root.title("Calculator")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvariable=scvalue, font="lucida 18 bold")
screen.pack(fill="x",pady=10, padx=10)
f=Frame(root,bg="sky blue")
b=Button(f,text='9',padx=20, pady=15, font="lucida 18 bold")
b.pack(side=LEFT, pady=10, padx=10)
b.bind("<Button-1>",click )
b=Button(f,text='8',padx=20, pady=15, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )
b=Button(f,text='7',padx=20, pady=15, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

f.pack()


f=Frame(root,bg="sky blue")
b=Button(f,text='6',padx=20, pady=15, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

b=Button(f,text='5',padx=20, pady=15, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

b=Button(f,text='4',padx=20, pady=15, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

f.pack()

f=Frame(root,bg="sky blue")
b=Button(f,text='3',padx=20, pady=15, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

b=Button(f,text='2',padx=20, pady=15, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

b=Button(f,text='1',padx=20, pady=15, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

f.pack()

f=Frame(root,bg="sky blue")
b=Button(f,text='-',padx=20, pady=18, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

b=Button(f,text='0',padx=20, pady=18, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

b=Button(f,text='+',padx=20, pady=18, font="lucida 18 bold")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

f.pack()

f=Frame(root,bg="sky blue")
b=Button(f,text='/',padx=14, pady=14, font="lucida 13 italic")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

b=Button(f,text='C',padx=14, pady=14, font="lucida 13 italic")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )

b=Button(f,text='*',padx=14, pady=14, font="lucida 13 italic")
b.pack(side=LEFT,pady=10, padx=10)
b.bind("<Button-1>",click )


b=Button(f,text='=',padx=14, pady=14, font="lucida 13 italic", fg="red")
b.pack(side=LEFT,pady=10, padx=10,)
b.bind("<Button-1>",click )
f.pack()
root.mainloop()