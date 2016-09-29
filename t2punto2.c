#include<stdio.h>
int main(){
int a,b,c,d,e,g,f;
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
	case 4:
		d=b/c;
		printf("La division es: %d\n",d);
		break;
	case 5:
		d=1;
		g=b;
		e=1;
		for(f=d;f<=c;f++){
			e=g*e;
		}
		printf("La potencia es: %d\n",e);
		break;
	case 6:
		printf("Ha salido del programa\n");
}
}
}


