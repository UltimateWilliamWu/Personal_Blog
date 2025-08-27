#include<stdio.h>

void fac(int i){
    
    if(i==1){
        printf("%d",i);
    }else{
        if(i%2==0){
            printf("%d\n",i);
            fac(i/2);
        }else{
            printf("%d\n",i);
            fac(i*3+1);
        }
    }
    
}

int Fib(int i){
    if(i==1||i==2){
        return 1;
    }else{
        return Fib(i-1)+Fib(i-2);
    }
}

int main(){
    for(int i=1;i<=12;i++){
        printf("Fib(%d)=%d\n",i,Fib(i));
        fac(Fib(i));
        printf("\n");
    }
}