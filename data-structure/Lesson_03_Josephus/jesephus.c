#include <stdio.h>

#define MAX_DEQUE_SIZE 5000

typedef int Element;
typedef struct DequeType {
    Element data[MAX_DEQUE_SIZE];
    int front, rear;
} DequeType;

void print_error(char* msg);
void init_deque(DequeType* deque);
void add_rear(DequeType* deque, Element item);
Element delete_front(DequeType* deque);
char is_empty(DequeType* deque);
char is_full(DequeType* deque);

int main(void)
{
    int n, k, i, j;
    DequeType deque;
    init_deque(&deque);
    scanf("%d %d", &n, &k);
    
    printf("<");
    for(i=1; i<=n; i++) add_rear(&deque, i);
    for(i=0; i<n-1; i++)
    {
        for(j=0; j<k-1; j++) add_rear(&deque, delete_front(&deque));
        printf("%d, ", delete_front(&deque));
    }
    printf("%d>\n", delete_front(&deque));

    return 0;
}

void init_deque(DequeType* deque)
{
    deque->front = deque->rear = 0;
}

void add_rear(DequeType* deque, Element item)
{
    deque->rear = (deque->rear + 1) % MAX_DEQUE_SIZE;
    deque->data[deque->rear] = item;
}

Element delete_front(DequeType* deque)
{
    deque->front = (deque->front + 1) % MAX_DEQUE_SIZE;
    return deque->data[deque->front];
}