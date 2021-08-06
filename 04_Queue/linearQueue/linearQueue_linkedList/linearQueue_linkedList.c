#include <stdio.h>
#include <stdlib.h>

#define STACK_MAX_SIZE 100

typedef int Data;

typedef struct QueueNode {
    Data data;
    struct QueueNode *link;
} QueueNode;

typedef struct Queue {
    QueueNode *front;
    QueueNode *rear;
} Queue;

void init_queue(Queue *queue);
char is_empty(Queue *queue);
char is_full(Queue *queue);
void enqueue(Queue *queue, Data data);
Data dequeue(Queue *queue);
Data peek(Queue *queue);

int main(void)
{
    Queue *queue;
    init_queue(queue);
    enqueue(queue, 1); printf("%d\n", peek(queue));
    enqueue(queue, 2); printf("%d\n", peek(queue));
    enqueue(queue, 3); printf("%d\n", peek(queue));
    dequeue(queue); printf("%d\n", peek(queue));
    dequeue(queue); printf("%d\n", peek(queue));
    dequeue(queue); printf("%d\n", peek(queue));
    return 0;
}

void print_error(char *msg)
{
    fprintf(stderr, "%s\n", msg);
    exit(1);
}

void init_queue(Queue *queue)
{
    queue->front = NULL;
    queue->rear = NULL;
}

char is_empty(Queue *queue)
{
    return (queue->front == NULL);
}

char is_full(Queue *queue)
{
    return 0;
}

void enqueue(Queue *queue, Data data)
{
    QueueNode *temp = (QueueNode *)malloc(sizeof(QueueNode));
    temp->data = data;
    temp->link = NULL;
    if (is_empty(queue))
    {
        queue->front = temp;
        queue->rear = temp;
    }
    else
    {
        queue->rear->link = temp;
        queue->rear = temp;
    }
}

Data dequeue(Queue *queue)
{
    if (is_empty(queue)) print_error("dequeue empty queue");
    QueueNode *temp = queue->front;
    Data data = temp->data;
    queue->front = queue->front->link;
    if (queue->front == NULL)
        queue->rear = NULL;
    free(temp);
    return data;
}

Data peek(Queue *queue)
{
    return queue->front->data;
}