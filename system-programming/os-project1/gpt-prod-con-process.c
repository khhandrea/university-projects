#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

#define NUM_DATA 500 // Number of data to generate

int main() {
    int fd[2]; // File descriptor for pipe
    pid_t pid; // Process ID of child process
    int data[NUM_DATA]; // Array to store generated data
    int i;

    // Generate random data
    for (i = 0; i < NUM_DATA; i++) {
        data[i] = rand() % 100;
    }

    // Create pipe
    if (pipe(fd) == -1) {
        perror("pipe");
        exit(1);
    }

    // Fork child process
    pid = fork();
    if (pid == -1) {
        perror("fork");
        exit(1);
    }

    if (pid == 0) { // Child process
        close(fd[1]); // Close write end of pipe
        int num;
        for (i = 0; i < NUM_DATA; i++) {
            // Read from pipe
            if (read(fd[0], &num, sizeof(int)) == -1) {
                perror("read");
                exit(1);
            }
            printf("%d ", num); // Print data
            usleep(1000); // Context switch
        }
        close(fd[0]); // Close read end of pipe
        exit(0);
    } else { // Parent process
        close(fd[0]); // Close read end of pipe
        for (i = 0; i < NUM_DATA; i++) {
            // Write to pipe
            if (write(fd[1], &data[i], sizeof(int)) == -1) {
                perror("write");
                exit(1);
            }
            usleep(1000); // Context switch
        }
        close(fd[1]); // Close write end of pipe
        wait(NULL); // Wait for child process to finish
        exit(0);
    }

    return 0;
}
