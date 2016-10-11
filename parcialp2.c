#include<stdio.h>
int main(){
float a,b,d,c;
float h=3.14;
int f=2;
printf("Escriba el radio:");
scanf("%f",&a);

b=a*f;
c=b*h;
d=(a*a)*h;


printf("el diametro: %f\n",b);

printf("la circunferencia es: %f\n",c);

printf("el area es: %f\n",d);
}
