// TODO : 걸쳐 있는 거 해결

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

#include "ku_fs_input.h"
// MAXS : size of array
// input : string

void findFailureKMP(char *substring, int *failure);
void matchKMP(char *string, char *substring, int *failure, int start, int interval, int *output);
void writeOutput(int pipefd, int *output);

int main(int argc, char *argv[]) {
    char *str; // system input : substring ot find
    int i; // system input : number of parallel processes

    float interval; // range where each process will find
    int step; // for loop indicator; each process' number
    int start; // index which each process starts finding
    int pos_buf; // buffer to be written from pipe
    pid_t *pid;
    int **pipefd;

    int *failure;
    int *output;

    pid_t wpid;
    int child_status;

    // check user arguments
    if (argc != 3) {
        printf("Argument error : expected 2, but got %d\n", argc - 1);
        return 0;
    }
    str = argv[1];
    i = atoi(argv[2]);

    failure = (int*)malloc(sizeof(int) * strlen(input));

    pid = (pid_t*)malloc(sizeof(pid_t) * i);
    pipefd = (int**)malloc(sizeof(int*) * i);
    for(int j = 0; j < i; j++)
        pipefd[j] = (int*)malloc(sizeof(int) * 2);
    interval = strlen(input) / (float)(i);
    output = (int*)malloc(sizeof(int*) * (int)(interval + 1));

    // find answer
    for(step = 0; step < i; step++) {
        if (pipe(pipefd[step]) == -1) {
            perror("pipe");
            exit(EXIT_FAILURE);
        }
        
        findFailureKMP(str, failure);
        if ((pid[step] = fork()) == 0) { // child
            close(pipefd[step][0]);
            start = (int)(interval * step);

            
            matchKMP(input, str, failure, start, interval, output);
            writeOutput(pipefd[step][1], output);
            close(pipefd[step][1]);

            exit(step);
        }
        else { // parent
            close(pipefd[step][1]);
        }
    }

    // get and print answer
    for(step = 0; step < i; step++) {
        wpid = waitpid(pid[step], &child_status, 0);
        if (WIFEXITED(child_status)) {
            while (read(pipefd[step][0], &pos_buf, sizeof(pos_buf))) {
                printf("%d\n", pos_buf);
            }
            close(pipefd[step][0]);
        }
        else {
            printf("Child %d terminated abnormally\n", wpid);
        }
    }

    return 0;
}

void findFailureKMP(char *substring, int *failure) {
    int i;
    int failureIndex = 0;

    failure[0] = 0;

    for (i = 1; i < strlen(substring); i++) {
        while (substring[i] != substring[failureIndex]) {
            if (failureIndex == 0) break;
            failureIndex = failure[failureIndex - 1];
        }
        if (substring[i] == substring[failureIndex]) {
            failure[i] = ++failureIndex;
        }
    }

    return;
}

void matchKMP(char *string, char *substring, int *failure, int start, int interval, int *output) {
    int cur = 0;
    int subStringLen = strlen(substring);
    int failureIndex = 0;
    int outputIndex = 0;

    for (int cur = start; cur < start + interval + subStringLen; cur++) {
        // jump with failure function
        while (string[cur] != substring[failureIndex]) {
            if (failureIndex == 0) break;
            failureIndex = failure[failureIndex - 1];
        }
        
        // check the validity
        if (string[cur] == substring[failureIndex]) {
            if (failureIndex == subStringLen - 1){
                output[outputIndex++] = cur - subStringLen + 1;
                failureIndex = failure[failureIndex];
            }
            else {
                failureIndex++;
            }
        }
    }
    output[outputIndex] = -1; // last index

    return;
}

void writeOutput(int pipefd, int *output) {
    for(int i = 0; i < MAXS; i++)
        if (output[i] == -1)
            return;
        else
            write(pipefd, &output[i], sizeof(output[i]));

    return;
}