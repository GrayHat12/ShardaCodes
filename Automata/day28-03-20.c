#include <stdio.h>

void main()
{
    char input[50],ch;
    int i;
    int curState = 0; // 0,1,2
    printf("Input String : ");
    scanf("%s",input);
    for(i=0;i<50&&input[i]!='\0';i++){
        ch = input[i];
        switch(curState){
            case 0: 
                if(ch=='a'){
                    curState = 1;
                }else if(ch=='b'){
                    curState = 0;
                }else{
                    printf("Not Accepted");
                    return;
                }
                break;
            case 1: 
                if(ch=='a'){
                    curState = 1;
                }else if(ch=='b'){
                    curState = 2;
                }else{
                    printf("Not Accepted");
                    return;
                }
                break;
            case 2: 
                if(ch=='a'){
                    curState = 1;
                }else if(ch=='b'){
                    curState = 0;
                }else{
                    printf("Not Accepted");
                    return;
                }
                break;
            default: printf("\nUnexpected Error"); return;
        }
    }
    if(curState==2){
        printf("STRING ACCEPTED");
    }else{
        printf("STRING REJECTED");
    }
}