import tkinter as tk
from tkinter import ttk
def on_click():
	label1.configure(text="Te dije que no   "+name.get())
	label1.configure(foreground='red')
	label1.configure(background='gold')
	boton.configure(state='disable')
pass
win = tk.Tk()
win.title("")
win.resizable(0,0)
#ttk.Label(win,text="Hola etiqueta").grid(row=0,column=0)
#ttk.Label(win,text="Diego F. Chavarro Sanchez").grid(row=0,column=1)
#ttk.Button(win,text="Click me",comman=on_click).grid(row=1,column=1)
label1=ttk.Label(win,text="Hola Label")
label1.grid(row=0,column=0)

boton7=ttk.Button(win,text="7",comman=on_click)
boton7.grid(row=4,column=3)

boton4=ttk.Button(win,text="4",comman=on_click)
boton4.grid(row=5,column=3)

boton1=ttk.Button(win,text="1",comman=on_click)
boton1.grid(row=6,column=3)

boton8=ttk.Button(win,text="8",comman=on_click)
boton8.grid(row=4,column=4)

boton5=ttk.Button(win,text="5",comman=on_click)
boton5.grid(row=5,column=4)

boton2=ttk.Button(win,text="2",comman=on_click)
boton2.grid(row=6,column=4)

boton0=ttk.Button(win,text="0",comman=on_click)
boton0.grid(row=7,column=4)

boton9=ttk.Button(win,text="9",comman=on_click)
boton9.grid(row=4,column=5)

boton6=ttk.Button(win,text="6",comman=on_click)
boton6.grid(row=5,column=5)

boton3=ttk.Button(win,text="3",comman=on_click)
boton3.grid(row=6,column=5)

botonpunto=ttk.Button(win,text=".",comman=on_click)
botonpunto.grid(row=7,column=5)

botondiv=ttk.Button(win,text="%",comman=on_click)
botondiv.grid(row=4,column=6)

botonmult=ttk.Button(win,text="%",comman=on_click)
botonmult.grid(row=5,column=6)

boton10=ttk.Button(win,text="9",comman=on_click)
boton10.grid(row=10,column=10)

name=tk.StringVar()
txtentry=ttk.Entry(win,textvariable=name)
txtentry.grid(row=1,column=0)

win.mainloop()
