#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

void fork07();
void fork08();
void fork10();

int main()
{
	fork10();

	return 0;
}

void fork07()
{
	// create zombie process
	// you have to set the option '&' to run background infinite loop
	// check with 'ps' command
	// to reap, use 'kill [pid]' command. you have to kill the parent process!!
	if (fork() == 0) {
		printf("Terminating Child, PID = %d\n", getpid());
		exit(0);
	}
	else {
		printf("Running Parent, PID = %d\n", getpid());
		while (1);
	}
}

void fork08()
{
	// terminate parent process first
	// no zombie is created
	if (fork() == 0) {
		printf("Running Child, PID = %d\n", getpid());
		while (1);
	}
	else {
		printf("Terminating Parent, PID = %d\n", getpid());
		exit(0);
	}
}

void fork10()
{
	// wait example
	int N = 10;
	pid_t pid[N], wpid;
	int i, child_status;
	for(i=0; i<N; i++)
		if ((pid[i] = fork()) == 0)
			exit(100 + i);
	for(i=0; i<N; i++)
	{
		wpid = wait(&child_status);
		if (WIFEXITED(child_status))
			printf("Child %d terminated with exit status %d\n", wpid, WEXITSTATUS(child_status));
		else
			printf("Child %d terminated abnormally\n", wpid);
	}

}
