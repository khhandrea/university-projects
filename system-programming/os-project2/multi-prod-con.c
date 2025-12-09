#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 32
#define NUM_PRODUCERS 5
#define NUM_CONSUMERS 5
#define NUM_DATA 1000

pthread_mutex_t mutex;

// Buffer
int buffer[BUFFER_SIZE];
int counter = 0;
int in = 0;
int out = 0;

// Semaphore
sem_t empty;
sem_t full;

void* producer(void* arg) {
    int producer_id = *((int*)arg);
    for (int i = 0; i < NUM_DATA; i++) {
        int item = rand() % 1000;  // Generate random data

        sem_wait(&empty);  // Wait for an empty slot in the buffer
        pthread_mutex_lock(&mutex);  // Acquire the mutex lock

        buffer[in] = item;
        printf("Producer %d produced item: %d\n", producer_id, item);
        in = (in + 1) % BUFFER_SIZE;
        counter++;

        pthread_mutex_unlock(&mutex);  // Release the mutex lock
        sem_post(&full);  // Signal that a new item is available in the buffer

        usleep(1000);
    }
    pthread_exit(NULL);
}

void* consumer(void* arg) {
    int consumer_id = *((int*)arg);
    for (int i = 0; i < NUM_DATA; i++) {
        sem_wait(&full);  // Wait for an item to be available in the buffer
        pthread_mutex_lock(&mutex);  // Acquire the mutex lock

        int item = buffer[out];
        printf("Consumer %d consumed item: %d\n", consumer_id, item);
        out = (out + 1) % BUFFER_SIZE;
        counter--;

        pthread_mutex_unlock(&mutex);  // Release the mutex lock
        sem_post(&empty);  // Signal that an empty slot is available in the buffer

        usleep(1000);
    }
    pthread_exit(NULL);
}

int main() {
    pthread_t producers[NUM_PRODUCERS];
    pthread_t consumers[NUM_CONSUMERS];
    int producer_ids[NUM_PRODUCERS];
    int consumer_ids[NUM_CONSUMERS];

    // Initialize mutex and semaphores
    pthread_mutex_init(&mutex, NULL);
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);

    // Create producer threads
    
    for (int i = 0; i < NUM_PRODUCERS; i++) {
        producer_ids[i] = i + 1;
        pthread_create(&producers[i], NULL, producer, &producer_ids[i]);
    }

    // Create consumer threads
    for (int i = 0; i < NUM_CONSUMERS; i++) {
        consumer_ids[i] = i + 1;
        pthread_create(&consumers[i], NULL, consumer, &consumer_ids[i]);
    }

    // Wait for producer threads to finish
    for (int i = 0; i < NUM_PRODUCERS; i++) {
        pthread_join(producers[i], NULL);
    }

    // Wait for consumer threads to finish
    for (int i = 0; i < NUM_CONSUMERS; i++) {
        pthread_join(consumers[i], NULL);
    }

    // Destroy mutex and semaphores
    pthread_mutex_destroy(&mutex);
    sem_destroy(&empty);
    sem_destroy(&full);

    printf("Work finished.\n");

    return 0;
}
