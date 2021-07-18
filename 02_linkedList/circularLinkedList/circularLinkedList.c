#include <stdio.h>
#include <stdlib.h>

typedef int DATA;
typedef struct NODE {
    DATA data;
    struct NODE *link;
} NODE;

NODE *insert(NODE *head, NODE *pre, DATA data);
NODE *delete_first(NODE *head);
NODE *delete(NODE *head, NODE *pre);
// void print_list(NODE *head);
// NODE *search_list(NODE *head, DATA data);
// NODE *concat_list(NODE *head1, NODE *head2);
// NODE *reverse_list(NODE *head);

int main(void)
{
    NODE *head = NULL;
    int i;

    head = insert(head, head, 1); // print_list(head);
    head = insert(head, head, 2); // print_list(head);
    head = insert(head, head, 3); // print_list(head);
    head = insert(head, head, 4); // print_list(head);
    // printf("%d\n", search_list(head, 3) == NULL);
    head = delete_first(head); // print_list(head);
    head = delete_first(head); // print_list(head);
    head = delete_first(head); // print_list(head);
    head = delete_first(head); // print_list(head);
    return 0;
}

NODE *insert(NODE *head, NODE *pre, DATA data)
{
    NODE *node = (NODE *)malloc(sizeof(NODE));
    node->data = data;
    if (head == NULL && pre == NULL)
    {
        node->link = node;
        head = node;        
    }
    else
    {
        node->link = pre->link;
        pre->link = node;
    }
    return head;
}

NODE *delete_first(NODE *head)
{
    NODE *removed;
    if (head == NULL) return NULL;
    removed = head;
    head = removed->link;
    free(removed);
    return head;
}

NODE *delete(NODE *head, NODE *pre)
{
    NODE *removed;
    removed = pre->link;
    pre->link = removed->link;
    free(removed);
    return head;
}

/*
void print_list(NODE *head)
{
    NODE *p;
    for(p = head; p != NULL; p = p->link)
        printf("%d->", p->data);
    printf("NULL \n");
}
*/