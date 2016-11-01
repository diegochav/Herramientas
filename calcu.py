import tkinter as tk
from tkinter import ttk
from tkinter import *

def on_buton1click():
	texto = name.get()
	name.set(texto+"1")
pass

def on_buton2click():
	texto = name.get()
	name.set(texto+"2")
pass

def on_buton3click():
	texto = name.get()
	name.set(texto+"3")
pass

def on_buton4click():
	texto = name.get()
	name.set(texto+"4")
pass

def on_buton5click():
	texto = name.get()
	name.set(texto+"5")
pass

def on_buton6click():
	texto = name.get()
	name.set(texto+"6")
pass

def on_buton7click():
	texto = name.get()
	name.set(texto+"7")
pass

def on_buton8click():
	texto = name.get()
	name.set(texto+"8")
pass

def on_buton9click():
	texto = name.get()
	name.set(texto+"9")
pass

def on_buton0click():
	texto = name.get()
	name.set(texto+"0")
pass

def on_butonpuntoclick():
	texto = name.get()
	name.set(texto+".")
pass

def on_butondivclick():
	texto = name.get()
	name.set(texto+"/")
pass

def on_butonmultclick():
	texto = name.get()
	name.set(texto+"*")
pass

def on_butonresclick():
	texto = name.get()
	name.set(texto+"-")
pass

def on_butonmasclick():
	texto = name.get()
	name.set(texto+"+")
pass

def on_butonceclick():
	texto = name.get()
	name.set(" ")
pass

def on_butonigualclick():
	texto = name.get()
	calculo =0
	calculo=eval(name.get())
	name.set("="+str(calculo))


win = tk.Tk()
win.title("CALCULADORA")
win.resizable(0,0)

label1=ttk.Label(win,text="CALCULADORA")
label1.grid(row=0,column=5)
label2=ttk.Label(win,text=" ")
label2.grid(row=3,column=5)
label3=ttk.Label(win,text=" ")
label3.grid(row=1,column=5)


boton7=ttk.Button(win,text="7",comman=on_buton7click)
boton7.grid(row=4,column=3)

boton4=ttk.Button(win,text="4",comman=on_buton4click)
boton4.grid(row=5,column=3)

boton1=ttk.Button(win,text="1",comman=on_buton1click)
boton1.grid(row=6,column=3)

boton8=ttk.Button(win,text="8",comman=on_buton8click)
boton8.grid(row=4,column=4)

boton5=ttk.Button(win,text="5",comman=on_buton5click)
boton5.grid(row=5,column=4)

boton2=ttk.Button(win,text="2",comman=on_buton2click)
boton2.grid(row=6,column=4)

boton0=ttk.Button(win,text="0",comman=on_buton0click)
boton0.grid(row=7,column=4)

boton9=ttk.Button(win,text="9",comman=on_buton9click,width=19)
boton9.grid(row=4,column=5)

boton6=ttk.Button(win,text="6",comman=on_buton6click,width=19)
boton6.grid(row=5,column=5)

boton3=ttk.Button(win,text="3",comman=on_buton3click,width=19)
boton3.grid(row=6,column=5)

botonpunto=ttk.Button(win,text=".",comman=on_butonpuntoclick,width=19)
botonpunto.grid(row=7,column=5)

botondiv=ttk.Button(win,text="%",comman=on_butondivclick)
botondiv.grid(row=4,column=6)

botonmult=ttk.Button(win,text="*",comman=on_butonmultclick)
botonmult.grid(row=5,column=6)

boton10=ttk.Button(win,text="-",comman=on_butonresclick)
boton10.grid(row=6,column=6)

boton10=ttk.Button(win,text="+",comman=on_butonmasclick)
boton10.grid(row=7,column=6)

boton10=ttk.Button(win,text="CE",comman=on_butonceclick)
boton10.grid(row=4,column=7)

boton10=ttk.Button(win,text="=",comman=on_butonigualclick)
boton10.grid(row=5,column=7)


name=tk.StringVar()
txtentry=ttk.Entry(win,textvariable=name)
txtentry.grid(row=2,column=5)


win.mainloop()
