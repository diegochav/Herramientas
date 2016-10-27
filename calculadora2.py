import tkinter as tk
from tkinter import ttk

def on_buton1click():
	texto=label2text.get()
	label2text.set(texto+"1")

pass

def on_buton2click():
	texto=label2text.get()
	label2text.set(texto+"2")

pass

def on_buton3click():
	texto=label2text.get()
	label2text.set(texto+"3")

pass

def on_buton4click():
	texto=label2text.get()
	label2text.set(texto+"4")

pass

def on_buton5click():
	texto=label2text.get()
	label2text.set(texto+"5")

pass

def on_buton6click():
	texto=label2text.get()
	label2text.set(texto+"6")

pass

def on_buton7click():
	texto=label2text.get()
	label2text.set(texto+"7")

pass

def on_buton8click():
	texto=label2text.get()
	label2text.set(texto+"8")

pass

def on_buton9click():
	texto=label2text.get()
	label2text.set(texto+"9")

pass

def on_buton0click():
	texto=label2text.get()
	label2text.set(texto+"0")

pass

def on_butonpuntoclick():
	texto=label2text.get()
	label2text.set(texto+".")

pass

def on_butondivclick():
	texto=label2text.get()
	label2text.set(texto+"%")

pass
def on_butonmultclick():
	texto=label2text.get()
	label2text.set(texto+"*")

pass
def on_butonresclick():
	texto=label2text.get()
	label2text.set(texto+"-")

pass
def on_butonmasclick():
	texto=label2text.get()
	label2text.set(texto+"+")

pass





win = tk.Tk()
win.title("")
win.resizable(0,0)
#ttk.Label(win,text="Hola etiqueta").grid(row=0,column=0)
#ttk.Label(win,text="Diego F. Chavarro Sanchez").grid(row=0,column=1)
#ttk.Button(win,text="Click me",comman=on_click).grid(row=1,column=1)

label1=ttk.Label(win,text="CALCULADORA")
label1.grid(row=0,column=5)

label2=ttk.Label(win,text="Numero 1")
label2.grid(row=1,column=4)
label2text=tk.StringVar()
label2.configure(textvar=label2text)

label4=ttk.Label(win,text="Operacion")
label4.grid(row=1,column=5)
label4text=tk.StringVar()
label4.configure(textvar=label4text)


label3=ttk.Label(win,text="Numero 2")
label3.grid(row=1,column=6)
label3text=tk.StringVar()
label3.configure(textvar=label3text)

label1=ttk.Label(win,text="Resultado")
label1.grid(row=2,column=5)




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

boton9=ttk.Button(win,text="9",comman=on_buton9click)
boton9.grid(row=4,column=5)

boton6=ttk.Button(win,text="6",comman=on_buton6click)
boton6.grid(row=5,column=5)

boton3=ttk.Button(win,text="3",comman=on_buton3click)
boton3.grid(row=6,column=5)

botonpunto=ttk.Button(win,text=".",comman=on_buton7click)
botonpunto.grid(row=7,column=5)

botondiv=ttk.Button(win,text="%",comman=on_buton7click)
botondiv.grid(row=4,column=6)

botonmult=ttk.Button(win,text="*",comman=on_buton7click)
botonmult.grid(row=5,column=6)

boton10=ttk.Button(win,text="-",comman=on_buton7click)
boton10.grid(row=6,column=6)

boton10=ttk.Button(win,text="+",comman=on_buton7click)
boton10.grid(row=7,column=6)

boton10=ttk.Button(win,text="CE",comman=on_buton7click)
boton10.grid(row=4,column=7)

boton10=ttk.Button(win,text="=",comman=on_buton7click)
boton10.grid(row=5,column=7)


#numero1=tk.StringVar()
#txtentry=ttk.Entry(win,textvariable=numero1,width=10)
#txtentry.grid(row=1,column=3)

#numero2=tk.StringVar()
#txtentry=ttk.Entry(win,textvariable=numero2,width=10)
#txtentry.grid(row=1,column=5)

#resultado=tk.StringVar()
#txtentry=ttk.Entry(win,textvariable=resultado,width=10)
#txtentry.grid(row=2,column=4)


win.mainloop()
