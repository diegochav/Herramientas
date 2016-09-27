#include<stdio.h>

int suma(int a, int b);
int resta(int a, int b);
int multiplicacion(int a, int b);

int main(){
	int numero1, numero2, operacion,resultado;
	while(1){
  	printf("Escriba primer numero\n");
	scanf("%d",&numero1);
	printf("Escriba segundo numero\n");
	scanf("%d",&numero2);
	printf("Escriba la operacion a realizar:\n 1:Suma\n 2:Resta\n 3:Multiplicacion\n 4:Salir \n");
	scanf("%d",&operacion);
	switch (operacion){
		case 1:
                	resultado=suma(numero1, numero2);
			printf("El resultado es: %d\n ",resultado);
			break;
		case 2:
			resultado=resta(numero1, numero2);
			printf("El resultado es: %d\n",resultado);
			break;
		case 3:
			resultado=multiplicacion(numero1, numero2);
			printf("El resultado es: %d\n",resultado);
			break;
		case 4:
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




