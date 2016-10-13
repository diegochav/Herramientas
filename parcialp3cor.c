#include<stdio.h>
int  main(){
int a,b,c,d,e,f;
printf("Escriba el numero de bases: ");
scanf("%d",&a);
printf("Escriba el numero de base 1: ");
scanf("%d",&b);
printf("Escriba el numero de base 2: ");
scanf("%d",&c);
printf("Escriba el numero de base 3: ");
scanf("%d",&d);

printf("Ingrese Modulo: ");
scanf("%d",&e);

printf(" 1:suma\n 2:resta\n 3:multiplicaion\n");
scanf("%d",&f);

switch (f){
	case 1:
		d=((b%e)+(c%e)+(d%e));
		printf("Suma es: %d\n",d);
		break;
	case 2:
		d=((b%e)-(c%e)-(d%e));
		printf("La resta: %d\n",d);
		break;
	case 3:
		d=((b%e)*(c%e)*(d%e));
		printf("multiplicacion: %d\n",d);
		break;
}
}


