#include<stdio.h>
int main(){
int a,b,c,d;
while (a!=6){
printf("Menu \n 1.suma \n 2.Resta \n 3.Multiplicacion \n 4.Div \n 5.Potencia \n 6.Salir \n");
scanf("%d",&a);
printf("Ingrese primer numero: \n");
scanf("%d",&b);
printf("Ingrese segundo numero: \n");
scanf("%d",&c);
switch (a){
	case 1:
		d=b+c;
		printf("La suma es: %d\n",d);
	break;
	case 2:
		d=b-c;
		printf("La resta es: %d\n",d);
	break;
	case 3:
		d=b*c;
		printf("La Multiplicacion es: %d\n",d);
	break;
		
}
}
}



