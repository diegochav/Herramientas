print("\n\nCALCULADORA\n 1:Suma\n 2:Resta\n 3:Multiplicacion\n 4:Division\n")

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
elif(valor < 1):
	print("No es una opcion: "+str(valor))
elif(valor > 4):
	print("No es una opcion: "+str(valor))

