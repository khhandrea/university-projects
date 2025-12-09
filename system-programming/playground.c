#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void fork_waitpid();

int main()
{
    fork_waitpid();

    return 0;
}

void fork_waitpid()
{
    int N = 10;
    int i, child_status;
    pid_t pid[N], wpid;

    for (i=0; i<N; i++) {
        if ((pid[i] = fork()) == 0) // child
            exit(100 + i);
    }

    for (i=0; i<N; i++) {
        wpid = waitpid(pid[i], &child_status, 0);
        if (WIFEXITED(child_status))
            printf("Child %d terminated with exit status %d\n", wpid, WEXITSTATUS(child_status));
        else
            printf("Child %d terminated abnormally.\n", wpid);
    }
}