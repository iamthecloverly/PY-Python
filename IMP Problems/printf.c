#include <stdlib.h>
#include <string.h>
#include <stdio.h>
int main()
{
    int a;
    scanf("%d",&a);
    char str[20];
    sprintf(str, "%d", a);
    puts(str);
}
