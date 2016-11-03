import tkinter as tk
import serial
from tkinter import ttk
def prender():
	global puerto
	puerto.write("a".encode())
def apagar():
	global puerto
	puerto.write("z".encode())

win = tk.Tk()
win.title("Conexion Arduino")
win.resizable(0,0)
puerto = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
label2=ttk.Label(win,text="Arduino")
label2.grid(row=0,column=1)
boton=ttk.Button(win,text="Prender", comman=prender)
boton.grid(row=1,column=1)
boton2=ttk.Button(win,text="Apagar",comman=apagar)
boton2.grid(row=2,column=1)


win.mainloop()
