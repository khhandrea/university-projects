#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#define DATA_NUM 500
#define BUF_SIZE 10

void *producer_thread();
void *consumer_thread();

int data_buf[BUF_SIZE];
int buf_num; // Current number of items of the buffer queue
int front, rear; // Index of input and output of the buffer queue
int count = 0; // The number of how many data are collected

int main(int argc, char* argv[]) {
    pthread_t thread_id[2];
    int status;

    srand((unsigned int)time(0));

    status = pthread_create(&thread_id[0], NULL, producer_thread, NULL);
    if (status != 0) {
        perror("pthread_create for producer_thread");
        exit(1);
    }

    status = pthread_create(&thread_id[1], NULL, consumer_thread, NULL);
    if (status != 0) {
        perror("pthread_create for consumer_thread");
        exit(1);
    }

    status = pthread_join(thread_id[0], NULL);
    if (status != 0) {
        perror("pthread_join for producer_thread");
        exit(1);
    }

    status = pthread_join(thread_id[1], NULL);
    if (status != 0) {
        perror("pthread_join for consumer_thraed");
        exit(1);
    }

    printf("\nAll threads are joined succefully, got %d data\n", count);

    return 0;
}

void *producer_thread() {
    int i, produced_data;

    for (i = 0; i<DATA_NUM; i++) {
        produced_data = rand() % 100;
        // produced_data = i; // Validation code for data loss or sequence

        while (buf_num == BUF_SIZE) {
            // printf("producer buffering..\n");
            usleep(100); // Context switch to wait the buffer to have a space
        }
        data_buf[front++] = produced_data;
        front %= BUF_SIZE;
        buf_num += 1;
    }
}

void *consumer_thread() {
    int i, produced_data;

    for (i = 0; i<DATA_NUM; i++) {
        while (buf_num == 0) {
            // printf("consumer buffering..\n");
            usleep(100); // Context switch to wait the buffer to be filled
        }

        produced_data = data_buf[rear++];
        rear %= BUF_SIZE;
        buf_num -= 1;
        printf("%d ", produced_data);
        count += 1; 
    }
}