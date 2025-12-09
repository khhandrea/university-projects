#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h> 
#include <unistd.h>
#include <pthread.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>

typedef int nodeItem;
typedef struct NODE {
	nodeItem data;
	struct NODE *next;
} node;

void *threadSearch(void *arg);
void findFailureKMP(char *substring, int *failure);
void matchKMP(char *substring, int *failure, int start, node *result);
void insertLinkedList(node *head, nodeItem item);
void saveFromLinkedList(node *head);
char *itoa(int number);

char *str, *input, *output;
int i, interval;
int *failure;
char *addr;

node result;

int main(int argc, char *argv[]) {
	int fd; // file descriptor
	int line; // # of line of file
	// float interval; // range where each process will find
	ssize_t ret; // return value
	char readBuf[5];
	char *readBufp = readBuf; // read buffer

	struct stat sb;

	pthread_t *threadIds;
	int *threadArg;
	int threadStep;
	int threadStatus;

	if (argc != 5) {
        return 0;
    }
    str = argv[1];
    i = atoi(argv[2]);
	input = argv[3];
	output = argv[4];

	result.data = -1;
	result.next = NULL;

	threadIds = (pthread_t*)malloc(sizeof(pthread_t) * i);
	threadArg = (int *)malloc(sizeof(pthread_t) * i);
	failure = (int*)malloc(sizeof(int) * strlen(str));

	// open ipnut file
	fd = open(input, O_RDONLY);
	if (fd < 0) {
		return 1;
	}

	// mmap
	if (fstat(fd, &sb) == -1) {
		return 1;
	}
	if (!S_ISREG(sb.st_mode)) {
		return 1;
	}
	addr = mmap(0, sb.st_size, PROT_READ, MAP_SHARED, fd, 0);
	if (addr == MAP_FAILED) {
		return 1;
	}

	// read the number of line
	ret = read(fd, readBufp, 6);
	if (ret < 0) {
		if (errno != EINTR) {
			close(fd);
			exit(1);
		}
		return 1;
	}
	line = atoi(readBufp);
	interval = sb.st_size - (line - 1) - 6 / (float)(i);
	close(fd);


	// create threads
	findFailureKMP(str, failure);
	for (threadStep=0; threadStep<i; threadStep++) {
		threadArg[threadStep] = threadStep;

		threadStatus = pthread_create(&threadIds[threadStep], NULL, threadSearch, &threadArg[threadStep]);
		if (threadStatus != 0) {
			return 1;
		}
	}

	// combine
	for (threadStep=0; threadStep<i; threadStep++) {
		threadStatus = pthread_join(threadIds[threadStep], NULL);
		if (threadStatus != 0) {
			return 1;
		}
	}

	// unmap & free
	if (munmap(addr, sb.st_size) == -1) {
		return 1;
	}
	free(threadIds);
	free(threadArg);
	free(failure);

	// save output
	saveFromLinkedList(&result);

	return 0;
}

void *threadSearch(void *arg) {
	int index = *(int *)arg;
	int start = index * interval;

	matchKMP(str, failure, start, &result);
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

void matchKMP(char *substring, int *failure, int start, node *result) {
    int cur = start;
	char *ptr = addr + cur + 6 + (int)(cur / 5);
    int subStringLen = strlen(substring);
    int failureIndex = 0;

	char readBuf = 0;

	while (cur < start + interval + subStringLen) {
		//read
		do {
			readBuf = *(ptr++);
		} while(readBuf == '\n');
		if(readBuf == 0) break;

        // jump with failure function
        while (readBuf != substring[failureIndex]) {
            if (failureIndex == 0) break;
            failureIndex = failure[failureIndex - 1];
        }
        
        // check the validity
        if (readBuf == substring[failureIndex]) {
            if (failureIndex == subStringLen - 1){
				insertLinkedList(result, cur - subStringLen + 1);
                failureIndex = failure[failureIndex];
            }
            else {
                failureIndex++;
            }
        }

		cur++;
    }
}

void insertLinkedList(node *head, nodeItem item) {
	node *prevNode = head;
	node *newNode = (node *)malloc(sizeof(node));
	newNode->data = item;
	newNode->next = NULL;

	// search
	while (prevNode->next != NULL) {
		if (prevNode->next->data > item) {
			newNode->next = prevNode->next;
			break;
		}
		prevNode = prevNode->next;
	}
	prevNode->next = newNode;

	return;
}

void saveFromLinkedList(node *head) {
	node *curNode = head;
	node *nextNode = curNode->next;
	int fd = open(output, O_WRONLY|O_CREAT|O_TRUNC);
	char *buf;
	int len;

	if (fd < 0) {
		exit(1);
	}

	while (nextNode != NULL) {
		curNode = nextNode;
		buf = itoa(curNode->data);
		len = strlen(buf);
		if (write(fd, buf, len) < 0) {
			exit(1);
		}
		free(buf);
		
		if(curNode->next != NULL) {
			buf = "\n";
			len = strlen(buf);
			if (write(fd, buf, len) < 0) {
				exit(1);
			}
		}

		nextNode = curNode->next;
		free(curNode);
	}

	return;
}

char *itoa(int number) {
	int i, len = 0;
	char temp;
	char *result = (char *)malloc(sizeof(char) * 10);
	for (i=0; i<10; i++) {
		result[i] = 0;
	}

	i = 0;
	while (number > 0) {
		len++;
		result[i++] = (char)((number % 10) + 48);
		number /= 10;
	}

	for(i=0; i<len/2; i++) {
		temp = result[i];
		result[i] = result[len - i - 1];
		result[len - i - 1] = temp;
	}
	
	return result;
}