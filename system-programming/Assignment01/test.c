#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void findFailureKMP(char* substring, int* failure);
void matchKMP(char* string, char* substring, int* failure, int startIndex, int interval, int* output);

int main() {
    char string[] = "abababcbdbaabcabcdababdbacabcabcdabbabcb";
    char substring[] = "abcabcd";
    int output[35];
    int *failure;
    failure = (int*)malloc(sizeof(int) * strlen(substring));

    findFailureKMP(substring, failure);
    matchKMP(string, substring, failure, 0, strlen(string), output);

    for (int i = 0; i < 35; i++)
        printf("%d ", output[i]);
    printf("\n");
}

void findFailureKMP(char* substring, int* failure) {
    int i;
    int j = 0;

    for (i = 0; i < strlen(substring); i++)
        failure[i] = 0;

    for (i = 1; i < strlen(substring); i++) {
        while(j > 0 && substring[i] != substring[j])
            j = failure[j - 1];
        if (substring[i] == substring[j])
            failure[i] = ++j;
    }

    return;
}

void matchKMP(char* string, char* substring, int* failure, int startIndex, int interval, int* output) {
    int curIndex = 0;
    int subStringLen = strlen(substring);
    int j = 0;
    int outputIndex = 0;

    for (int curIndex = startIndex; curIndex < startIndex + interval; curIndex++) {
        while (j > 0 && string[curIndex] != substring[j])
            j = failure[j - 1];
        if (string[curIndex] == substring[j]) {
            if (j == subStringLen - 1){
                output[outputIndex++] = curIndex - (subStringLen - 1);
                j = failure[j];
            }
            else {
                j++;
            }
        }
    }
    output[outputIndex] = -1;

    return;
}