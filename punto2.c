#include<stdio.h>
int main(){

int a=0,b=0,pos=0,neg=0,par=0,imp=0;
for (a=0;a<10;a++){
	printf("Ingrese el valor: \n");
	scanf("%d",&b);
		if (b>=0){
		pos=pos+1;
			if(b%2==0){
				par=par+1;
				}
			else {
				imp=imp+1;
			}
		}
		else {
		neg=neg+1;
			if(b%2==0){
				par=par+1;
			}
			else{
				imp=imp+1;
			}
		}	
}
printf("\nLos numeros positivos son: %d\n",pos);
printf("\nLos numeros negativos son: %d\n",neg);
printf("\nLos numeros pares son: %d\n",par);
printf("\nLos numeros impares son: %d\n",imp);

}
