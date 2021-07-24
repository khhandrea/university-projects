#include <stdio.h>
#include <stdlib.h>
#define MAX_QUEUE_SIZE 5

typedef int Element;
typedef struct {
    Element data[MAX_QUEUE_SIZE];
    int front, rear;
} QueueType;

void print_error(char* msg);
void init_queue(QueueType* queue);
char is_empty(QueueType* queue);
char is_full(QueueType* queue);
void print_queue(QueueType* queue);
void enqueue(QueueType* queue, Element item);
Element dequeue(QueueType* queue);

int main(void)
{
    QueueType queue;
    int element;

    init_queue(&queue);
    printf("--데이터 추가 단계--\n");
    while(!is_full(&queue))
    {
        printf("정수를 입력하시오: ");
        scanf("%d", &element);
        enqueue(&queue, element);
        print_queue(&queue);
    }
    printf("큐는 포화상태입니다.\n\n");

    printf("--데이터 삭제--\n");
    while(!is_empty(&queue))
    {
        element = dequeue(&queue);
        printf("꺼내진 정수: %d\n", element);
        print_queue(&queue);
    }
    printf("큐는 공백상태입니다.\n");

    return 0;
}

void print_error(char* msg)
{
    fprintf(stderr, "%s\n", msg);
    exit(1);
}

void init_queue(QueueType* queue)
{
    queue->front = queue->rear = 0;
}

char is_empty(QueueType* queue)
{
    return (queue->front == queue->rear);
}

char is_full(QueueType* queue)
{
    return ((queue->rear + 1) % MAX_QUEUE_SIZE == queue->front);
}

void print_queue(QueueType* queue)
{
    int i = queue->front;
    printf("front : %2d, rear : %2d\n", queue->front, queue->rear);
    if(!is_empty(queue))
    {
        printf("[");
        do
        {
            i = (i + 1) % MAX_QUEUE_SIZE;
            printf(" %2d ", queue->data[i]);
            if(i == queue->rear) break;
        } while(i != queue->front);
        printf("]\n");
    }
}

void enqueue(QueueType* queue, Element item)
{
    if(is_full(queue)) print_error("The queue is full");
    queue->rear = (queue->rear+1) % MAX_QUEUE_SIZE;
    queue->data[queue->rear] = item;
}

Element dequeue(QueueType* queue)
{
    if(is_empty(queue)) print_error("The queue is empty");
    queue->front = (queue->front + 1) % MAX_QUEUE_SIZE;
    return queue->data[queue->front];
}