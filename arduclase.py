import tkinter as tk
import serial
from tkinter import ttk

def on_click():
	global puerto
	puerto.open()
	val = puerto.read(2)
	print (val)
	if (val<b'x\17x\d4'):
		label1.configure(background = 'white')
	puerto.close()
win = tk.Tk()
win.title("Conexion Arduino")
win.resizable(0,0)
puerto = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
puerto.close()
label1=ttk.Label(win,text="000")
label1.grid(row=1,column=2)
label3=ttk.Label(win,text="000")
label3.grid(row=1,column=3)
label4=ttk.Label(win,text="000")
label4.grid(row=1,column=4)
label2=ttk.Label(win,text="000")
label2.grid(row=1,column=5)
boton=ttk.Button(win,text="Leer",command=on_click)
boton.grid(row=0,column=1)






win.mainloop()
