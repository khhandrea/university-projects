#include <stdio.h>
#include <stdlib.h>
#define LIST_MAX_SIZE 100
typedef int DATA;
typedef struct Node {
    DATA data;
    struct Node* next;
} NODE;

void print_error(char* msg);
NODE* create_list(DATA item);
char get_length(NODE* head);
NODE* get_entry(NODE* head, char pos);
NODE* insert(NODE* head, char pos, NODE node);
NODE* delete(NODE* head, char pos);
NODE* clear_list(NODE* head);
void free_list(NODE* head);
void print_list(NODE* head);

int main(void)
{
    NODE* head = create_list(10);
    printf("length : %d\n", get_length(head));
    printf("0x00 : %d\n", get_entry(head, 0)->data);
    print_list(head);

    return 0;
}

void print_error(char* msg)
{
    fprintf(stderr, "%s\n", msg);
}

NODE* create_list(DATA item)
{
    NODE* head = (NODE *)malloc(sizeof(NODE));
    head->data = item;
    head->next = NULL;
    return head;
}

char get_length(NODE* head)
{
    NODE* temp_node = head;
    char count;
    for(count=1; temp_node->next != NULL; count++) temp_node = temp_node->next;
    return count;
}

NODE* get_entry(NODE* head, char pos)
{
    if(pos >= get_length(head)) print_error("exceed memory range");
    NODE* temp_node = head;
    char count;
    for(count=0; count<pos; count++) temp_node = temp_node->next;
    return temp_node;
}

// NODE* insert(NODE* head, char pos, NODE node);
// NODE* delete(NODE* head, char pos);
// NODE* clear_list(head);
// void free_list(head);

void print_list(NODE* head)
{
    NODE* temp_node = head;
    char count=0;
    while(1)
    {
        printf("0x%02d : %d\n", count, temp_node->data);
        if(temp_node->next != NULL) temp_node = temp_node->next;
        else break;
        count += 1;
    }
}