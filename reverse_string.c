#include <stdio.h>
#include <stdlib.h>

void str_rev(char *s);

int main(){
    char s[1000];

    scanf("%s", s);

    str_rev(s);

    printf("%s",s);

    return 0;
}

void str_rev(char *s){
    int i = 0,j = 0;
    char temp;

    while(s[j] != '\0')j++;
    j--;
    while(i<j){
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
        i++;j--;
    }

    return;
}
