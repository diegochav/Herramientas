#include<stdio.h>

int suma(int a, int b);
int resta(int a, int b);
int multiplicacion(int a, int b);
int potencia(int a, int b);
//int factorial(int a);

int main(){
	int numero1, numero2, operacion,resultado;
	while(1){
	printf("CALCULADORA\n 1:Suma\n 2:Resta\n 3:Multiplicacion\n 4:Potencia\n 5:Factorial\n 6:Salir\n Escriba el numero de la operacion a realizar: ");
	scanf("%d",&operacion);
	switch (operacion){
		case 1:
			printf("Escriba primer numero:\n");
			scanf("%d",&numero1);
			printf("Escriba segundo numero:\n");
			scanf("%d",&numero2);
                	resultado=suma(numero1, numero2);
			printf("El resultado es: %d\n ",resultado);
			break;
		case 2:
			printf("Escriba primer numero:\n");
			scanf("%d",&numero1);
			printf("Escriba segundo numero:\n");
			scanf("%d",&numero2);
			resultado=resta(numero1, numero2);
			printf("El resultado es: %d\n",resultado);
			break;
		case 3:
			printf("Escriba primer numero:\n");
			scanf("%d",&numero1);
			printf("Escriba segundo numero:\n");
			scanf("%d",&numero2);
			resultado=multiplicacion(numero1, numero2);
			printf("El resultado es: %d\n",resultado);
			break;
		case 4:
			printf("Escriba un numero:\n");
			scanf("%d",&numero1);
			printf("Escriba la potencia para el numero anterior:\n");
			scanf("%d",&numero2);
			resultado=potencia(numero1, numero2);
			printf("El resultado es: %d\n", resultado);
			break;
		//case 5:
		//	printf("Escriba un numero:\n");
		//	scanf("%d",&numero1);
		//	resultado=factorial(numero1);
		//	printf("El resultado es: %d\n", resultado);
		//	break;






		case 6:
			printf("Ha salido de la calculadora\n");
			return 0;
			break;

         }
     }
}
int suma(int numero1, int numero2){
	return numero1+numero2;
}
int resta(int numero1, int numero2){
	return numero1-numero2;
}
int multiplicacion(int numero1, int numero2){
	int a=0;

	for(int i=0;i<numero2;i++){
		a=a+numero1;
		}
	return a;
}
int potencia(int numero1, int numero2){
	int a=numero1;
	int b=0;
	for(int i=0;i<numero2;i++){
		a=a+b;
		b=0;
		for(int f=1;f<numero1;f++){
			b=b+a;
		}
	}
	return a;
}

