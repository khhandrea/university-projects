#include <stdio.h>
#include <stdlib.h>

#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

#define MAX_ID 5

int main(void)
{
    key_t ipckey;
    int mqdes, i;
    size_t buf_len;
    struct {
        long id;
        int value;
    } mymsg;

    buf_len = sizeof(mymsg.value);

    ipckey = ftok("./src/port", 8000);
    mqdes = msgget(ipckey, IPC_CREAT|0600);

    if (mqdes < 0 ) {
        perror("msgget()");
        exit(0);
    }

    for (i = 0; i <= MAX_ID; i++) {
        mymsg.id = i + 1;
        mymsg.value = i * 3;
        printf("Sending a message (id: %ld, value: %d)\n", mymsg.id, mymsg.value);

        if (msgsnd(mqdes, &mymsg, buf_len, 0) == -1) {
            perror("msgsnd()");
            exit(0);
        }
    }
    
    return 0;
}