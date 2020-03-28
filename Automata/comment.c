#include<stdio.h>

int isComment(char* arr) // for // comment format
{
    int cstate = 0; // 0,1,2
    int i,count=0;
    char ch;
    for(i=0;arr[i]!='\0' && count<2;i++)
    {
        ch = arr[i];
        if(ch=='/')
        {
            count+=1;
        }
        else if(ch!=' '){
            return 0;
        }
    }
    if(count==2)
        return 1;
    return 0;
}

void main()
{
    char str[500];
    printf("TOKEN : ");
    scanf("%s",str);
    if(isComment(str)==1){
        printf("\nIS A COMMENT");
    }else{
        printf("\nIS NOT A COMMENT");
    }
}