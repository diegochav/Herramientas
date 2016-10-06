import math
def cal():
	print("\n\nCALCULADORA\n 1:Suma\n 2:Resta\n 3:Multiplicacion\n 4:Division\n 5:Exponencial\n 6:Funcion Coseno\n 7:De grados a radianes\n 10:Salir\n")

	valor = int( input("escriba una opcion: "))

	if(valor == 1):
		numero1 = int(input("Escriba un numero: "))
		numero2 = int(input("Escriba otro numero: "))
		resultado = numero1+numero2
		print("El resultado es: "+str(resultado))
	elif(valor == 2):
		numero1 = int(input("Escriba un numero: "))
		numero2 = int(input("Escriba otro numero: "))
		resultado = numero1-numero2
		print("El resultado es: "+str(resultado))
	elif(valor == 3):
		numero1 = int(input("Escriba un numero: "))
		numero2 = int(input("Escriba otro numero: "))
		resultado = numero1*numero2
		print("El resultado es: "+str(resultado))
	elif(valor == 4):
		numero1 = int(input("Escriba un numero: "))
		numero2 = int(input("Escriba otro numero: "))
		resultado = numero1/numero2
		print("El resultado es: "+str(resultado))
	elif(valor == 5):
		numero1 = int(input("Escriba un numero: "))
		resultado = math.exp(numero1)
		print("El resultado es: "+str(resultado))
	elif(valor == 6):
		numero1 = int(input("Escriba un numero: "))
		resultado = math.cos(numero1)
		print("El resultado es en radianes: "+str(resultado))
	elif(valor == 7):
		numero1 = int(input("Escriba los grados: "))
		resultado = math.radians(numero1)
		print("El numero ingresado en radianes es:"+str(resultado))
	elif(valor < 1):
		print("No es una opcion: "+str(valor))
	elif(valor == 10):
		print("Salio de la calculadora ")	
	return valor
while (cal() !=10):
	pass
