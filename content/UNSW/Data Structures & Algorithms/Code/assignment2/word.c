#include<stdio.h>
#include<stdbool.h>
#include<string.h>

bool hasRepeatedLetter(char A[]){
    int size=strlen(A);
    for(int i=0;i<size;i++){
        for(int j=i+1;j<size;j++){
            if(A[i]==A[j]){
                return true;
            }
        }
    }
    return false;
}


int main(void){
    char str[32];
    printf("Enter a word:");
    scanf("%31s",str);
    bool result=hasRepeatedLetter(str);
    if(result==1){
        printf("yes");
    }else{
        printf("no");
    }
    return 0;
}