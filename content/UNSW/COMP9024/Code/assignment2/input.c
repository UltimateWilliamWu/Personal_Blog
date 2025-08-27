#include<stdio.h>

int main(void){
    int input;
    printf("Please input a number:");
    scanf("%d",&input);
    if(input>0){
        printf("\n%d",input);
    }
    return 0;
}