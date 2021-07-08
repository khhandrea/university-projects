#include <stdio.h>
#include <stdlib.h>

#define MAX_DEQUE_SIZE 5

typedef int Element;
typedef struct {
    Element data[MAX_DEQUE_SIZE];
    int front, rear;
} DequeType;

void print_error(char* msg);
void init_deque(DequeType* deque);
void add_front(DequeType* deque, Element item);
void add_rear(DequeType* deque, Element item);
Element delete_front(DequeType* deque);
Element delete_rear(DequeType* deque);
Element get_front(DequeType* deque);
Element get_rear(DequeType* deque);
char is_empty(DequeType* deque);
char is_full(DequeType* deque);

int main(void)
{
    DequeType deque;
    
    return 0;
}

void print_error(char* msg)
{
    fprintf(stderr, "%s\n", msg);
    exit(1);
}

void init_deque(DequeType* deque)
{
    deque->front = deque->rear = 0;
}

void add_front(DequeType* deque, Element item)
{
    if(is_full(deque)) print_error("The deque is full");
    deque->data[deque->front] = item;
    deque->front = (deque->front - 1 + MAX_DEQUE_SIZE) % MAX_DEQUE_SIZE;
}

void add_rear(DequeType* deque, Element item)
{
    if(is_full(deque)) print_error("The deque is full");
    deque->rear = (deque->rear + 1) % MAX_DEQUE_SIZE;
    deque->data[deque->rear] = item;
}

Element delete_front(DequeType* deque)
{
    if(is_empty(deque)) print_error("The deque is empty");
    deque->front = (deque->front + 1) % MAX_DEQUE_SIZE;
    return deque->data[deque->front];
}

Element delete_rear(DequeType* deque)
{
    if(is_empty(deque)) print_error("The deque is empty");
    deque->rear = (deque->rear - 1) % MAX_DEQUE_SIZE;
    return deque->data[deque->rear];
}

Element get_front(DequeType* deque)
{
    if(is_empty(deque)) print_error("The deque is empty");
    return deque->data[(deque->front + 1) % MAX_DEQUE_SIZE];
}

Element get_rear(DequeType* deque)
{
    if(is_empty(deque)) print_error("The deque is empty");
    return deque->data[(deque->rear) % MAX_DEQUE_SIZE];
}

char is_full(DequeType* deque)
{
    return (deque->front == (deque->rear + 1) % MAX_DEQUE_SIZE);
}

char is_empty(DequeType* deque)
{
    return (deque->front == deque->rear);
}