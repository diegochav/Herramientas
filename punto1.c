#include<stdio.h>
int main(){

int a;
int b;
printf("Ingrese primer numero: \n");
scanf("%d",&a);
printf("Ingrese segundo numero: \n");
scanf("%d",&b);
if (a<b){
	printf("\nEl numero mayor es: %d\n", b);
}
if (a>b){
	printf("\nEl numero mayor es: %d\n", a);
}
}
