#include<stdio.h>
int main(){
int a;
printf("Escriba un numero: \n");
scanf("%d",&a);
while(a<=0){
	printf("El numero es menor: %d\n",a);
	printf("Escriba otro numero: \n");
	scanf("%d",&a);
}
printf("el numero es mayor \n");
return 0;
}


