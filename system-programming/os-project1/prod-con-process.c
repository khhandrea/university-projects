#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>

#define DATA_NUM 500

int main(int argc, char* argv[]) {
    pid_t wpid;
    int pipefd[2];
    int status;

    int produced_data;
    int i;

    // Randimoize the seed
    srand((unsigned int)time(0));

    // Make pipe
    if (pipe(pipefd) == -1) {
        perror("pipe");
        exit(1);
    }
    
    if (fork() == 0) { // Child (producer)
        close(pipefd[0]);
        
        for(i=0; i<DATA_NUM; i++) {
            produced_data = rand() % 100;
            produced_data = i; // Validation code for data loss or sequence
            write(pipefd[1], &produced_data, sizeof(produced_data));
            usleep(100); // Context switch
        }
        close(pipefd[1]);
        exit(1);
    }
    else { // Parent (consumer)
        close(pipefd[1]);

        for(i=0; i<DATA_NUM; i++) {
            // Read and print the data from the child process through the pipe
            read(pipefd[0], &produced_data, sizeof(produced_data));
            usleep(100); // Context switch
            printf("%d ", produced_data);
        }

        // Collect for child process
        wpid = waitpid(pid, &status, 0);
        if (WIFEXITED(status)) {
            printf("\nChild %d terminated successfully, got %d data\n", wpid, i);
            close(pipefd[0]);
        }
    }

    return 0;
}