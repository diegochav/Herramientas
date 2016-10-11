#include<stdio.h>
int  main(){
int a,c,d,f;
printf("Escriba un bumero de datos: ");
	scanf("%d",&a);
f=0;
for(int i=0;i<a;i++){
	printf("Escriba dato: ");
	scanf("%d",&d);
	f=d+f;
}
d=f/a;
printf("Sumatoria: %d",f);

printf("promedio: %d\n",d);
}


