#include <stdio.h>
#include <stdlib.h>

void print_error(char* msg)
{
    fprintf(stderr, "%s\n", msg);
    exit(1);
}

int main(void)
{
    print_error("this is error");
    return 0;
}