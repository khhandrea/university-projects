#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

#define BUFFER_SIZE 100 // Size of shared buffer
#define NUM_DATA 500 // Number of data to generate

int buffer[BUFFER_SIZE]; // Shared buffer
int in = 0; // Index of next free slot in buffer
int out = 0; // Index of next filled slot in buffer
int count = 0; // Number of items in buffer

// Generate random data
void *producer_thread(void *arg) {
    int i, num;
    for (i = 0; i < NUM_DATA; i++) {
        num = rand() % 100;
        while (count == BUFFER_SIZE) ; // Wait for buffer to have free space
        buffer[in] = num;
        in = (in + 1) % BUFFER_SIZE;
        count++;
        usleep(1000); // Context switch
    }
    pthread_exit(NULL);
}

// Print data from buffer
void *consumer_thread(void *arg) {
    int i, num;
    for (i = 0; i < NUM_DATA; i++) {
        while (count == 0) ; // Wait for buffer to have data
        num = buffer[out];
        out = (out + 1) % BUFFER_SIZE;
        count--;
        printf("%d ", num);
        usleep(1000); // Context switch
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t producer_tid, consumer_tid;
    srand(time(NULL)); // Seed random number generator

    // Create producer and consumer threads
    if (pthread_create(&producer_tid, NULL, producer_thread, NULL) != 0) {
        perror("pthread_create");
        exit(1);
    }
    if (pthread_create(&consumer_tid, NULL, consumer_thread, NULL) != 0) {
        perror("pthread_create");
        exit(1);
    }

    // Wait for threads to finish
    if (pthread_join(producer_tid, NULL) != 0) {
        perror("pthread_join");
        exit(1);
    }
    if (pthread_join(consumer_tid, NULL) != 0) {
        perror("pthread_join");
        exit(1);
    }

    return 0;
}
