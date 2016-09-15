#include<stdio.h>
int main(){
char letra1,letra2;
printf("Dame una letra: \n");
scanf("%c%*c",&letra1);
printf("Dame otra letra: \n");
scanf("%c",&letra2);
printf("Las letras son: \n");
while((letra1<=letra2)){
printf("%3c",letra1);
letra1++;
}
while((letra2<=letra1)){
printf("%3c",letra2);
letra2++;
}
printf("\n");
return 0;
}

