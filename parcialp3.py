z = int(input("Escriba el numero de bases: "))
a = int(input("Escriba una base: "))
b = int(input("Escriba una base: "))
c = int(input("Escriba una base: "))
modulo = int(input("Escriba un modulo: "))
d = int(a%modulo)
e = int(b%modulo)
f = int(c%modulo)
print(" 1:Suma\n 2:Resta\n 3:Multiplicacion\n")
op = int(input("Elija una operacion: "))
if(op==1):
	res=int(d+e+f)
	print("La suma es: "+str(res))
elif(op==2):
	res=int(d-e-f)
	print("La resta es: "+str(res))
elif(op==3):
	res=int(d*e*f)
	print("La multiplicacion es: "+str(res))

