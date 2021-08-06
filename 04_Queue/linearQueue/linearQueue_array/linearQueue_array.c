#include <stdio.h>
#include <stdlib.h>
#define MAX_QUEUE_SIZE 5

typedef int Data;
typedef struct {
    int front;
    int rear;
    Data data[MAX_QUEUE_SIZE];
} QueueType;

void error(char* msg);
void init_queue(QueueType* queue);
void queue_print(QueueType* queue);
char is_full(QueueType* queue);
char is_empty(QueueType* queue);
void enqueue(QueueType* queue, Data data);
Data dequeue(QueueType* queue);

int main(void)
{
    int data = 0;
    QueueType queue;

    init_queue(&queue);
    enqueue(&queue, 10); queue_print(&queue);
    enqueue(&queue, 20); queue_print(&queue);
    enqueue(&queue, 30); queue_print(&queue);

    data = dequeue(&queue); queue_print(&queue);
    data = dequeue(&queue); queue_print(&queue);
    data = dequeue(&queue); queue_print(&queue);
    
    return 0;
}

void print_error(char *msg)
{
    fprintf(stderr, "%s\n", msg);
    exit(1);
}

void init_queue(QueueType* queue)
{
    queue->front = queue->rear = -1;
}

void queue_print(QueueType* queue)
{
    int i;
    printf("[");
    for(i=queue->front+1; i<=queue->rear; i++) printf(" %2d ", queue->data[i]);
    printf("]\n");
}

char is_full(QueueType* queue)
{
    return (queue->rear == MAX_QUEUE_SIZE - 1);
}

char is_empty(QueueType* queue)
{
    return (queue->front == queue->rear);
}

void enqueue(QueueType* queue, Data data)
{
    if(is_full(queue))
    {
        print_error("The queue is full");
        return;
    }
    queue->data[++(queue->rear)] = data;
    return;
}

Data dequeue(QueueType* queue)
{
    if(is_empty(queue))
    {
        print_error("The queue is empty");
        return 0;
    }
    return queue->data[++(queue->front)];
}