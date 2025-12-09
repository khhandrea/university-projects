#include <stdio.h>

#define MAX_STACK_SIZE 51

typedef struct STACK {
    char data[MAX_STACK_SIZE];
    char top;
} STACK;

void push(STACK* stack, char item);
char pop(STACK* stack);
char is_empty(STACK* stack);

int main(void)
{
    int count, i;
    char input;
    STACK stack = {.top = -1};

    scanf("%d", &count);
    getchar(); // clear buffer
    for(i=0; i<count; i++) {
        stack.top = -1;
        while(1) {
            scanf("%c", &input);

            if(input == '(') {
                push(&stack, '(');
            }
            else if(input == ')') {
                if(pop(&stack) == -1) {
                    printf("NO\n");
                    while(getchar()!='\n'); // clear buffer
                    break;
                }
            }
            else if(input == '\n') {
                if(is_empty(&stack)) printf("YES\n");
                else printf("NO\n");
                break;
            }
        }
    }
    return 0;    
}

void push(STACK* stack, char item)
{
    stack->top += 1;
    stack->data[stack->top] = item;
}

char pop(STACK* stack)
{
    if(stack->top == -1) return -1;
    else return stack->data[stack->top--];
}

char is_empty(STACK* stack)
{
    if(stack->top == -1) return 1;
    else return 0;
}