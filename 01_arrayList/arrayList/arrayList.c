#include <stdio.h>
#include <stdlib.h>

#define LIST_MAX_SIZE 100
typedef int Data;
typedef struct ArrayList {
    Data array[LIST_MAX_SIZE];
    int size;
} ArrayList;

void print_error(char *msg);
void list_init(ArrayList *L);
char is_empty(ArrayList *L);
char is_full(ArrayList *L);
Data get_entry(ArrayList *L, int pos);
void print_list(ArrayList *L);
void insert(ArrayList *L, int pos, Data data);
Data delete(ArrayList *L, int pos);

int main(void)
{
    ArrayList *head;
    list_init(head);

    insert(head, 0, 10); print_list(head);
    insert(head, 0, 20); print_list(head);
    insert(head, 0, 30); print_list(head);
    insert(head, head->size, 40); print_list(head);
    delete(head, 0); print_list(head);
    return 0;
}

void print_error(char *msg)
{
    fprintf(stderr, "%s\n", msg);
    exit(1);
}

void list_init(ArrayList *L)
{
    L->size = 0;
}

char is_empty(ArrayList *L)
{
    return L->size == 0;
}

char is_full(ArrayList *L)
{
    return L->size == LIST_MAX_SIZE;
}

Data get_entry(ArrayList *L, int pos)
{
    if (pos < 0 || pos >= LIST_MAX_SIZE) print_error("position error");
    return L->array[pos];
}

void print_list(ArrayList *L)
{
    int i;
    for(i=0; i<L->size; i++)
        printf("%d ->", L->array[i]);
    printf("\n");
}

void insert(ArrayList *L, int pos, Data data)
{
    int i;
    if (is_full(L))
        print_error("list overflow");
    if (pos < 0 || pos > L->size)
        print_error("position error");
    for(i = L->size-1; i >= pos; i--)
        L->array[i + 1] = L->array[i];
    L->array[pos] = data;
    L->size++;
}

Data delete(ArrayList *L, int pos)
{
    Data data;
    int i;
    if (pos < 0 || pos >= L->size)
        print_error("position error");
    data = L->array[pos];
    for(i = pos; i < (L->size - 1); i++)
        L->array[i] = L->array[i + 1];
    L->size--;
    return data;
}