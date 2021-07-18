#include <stdio.h>
#include <stdlib.h>

#define STACK_MAX_SIZE 100

typedef int DATA;

typedef struct StackNode {
    DATA data;
    struct StackNode *link;
} StackNode;

typedef struct Stack {
    StackNode *top;
} Stack;

void init_stack(Stack *stack);
char is_empty(Stack *stack);
char is_full(Stack *stack);
void push(Stack *stack, DATA data);
DATA pop(Stack *stack);
DATA peek(Stack *stack);

int main(void)
{
    Stack *stack;
    init_stack(stack);
    push(stack, 1); printf("%d\n", peek(stack));
    push(stack, 2); printf("%d\n", peek(stack));
    push(stack, 3); printf("%d\n", peek(stack));
    pop(stack); printf("%d\n", peek(stack));
    pop(stack); printf("%d\n", peek(stack));
    pop(stack); printf("%d\n", peek(stack));
    return 0;
}

void print_error(char *msg)
{
    fprintf(stderr, "%s\n", msg);
    exit(1);
}

void init_stack(Stack *stack)
{
    stack->top = NULL;
}

char is_empty(Stack *stack)
{
    return (stack->top == NULL);
}

char is_full(Stack *stack)
{
    return 0;
}

void push(Stack *stack, DATA data)
{
    StackNode *temp = (StackNode *)malloc(sizeof(StackNode));
    temp->data = data;
    temp->link = stack->top;
    stack->top = temp;
}

DATA pop(Stack *stack)
{
    if (is_empty(stack)) print_error("pop empty stack");
    StackNode *temp = stack->top;
    DATA data = temp->data;
    stack->top = stack->top->link;
    free(temp);
    return data;
}

DATA peek(Stack *stack)
{
    return stack->top->data;
}