#include <stdio.h>
#include <stdlib.h>

typedef int Data;
typedef struct Node {
    Data data;
    struct Node *link;
} Node;

Node *insert(Node *head, Node *pre, Data data);
Node *delete_first(Node *head);
Node *delete(Node *head, Node *pre);
// void print_list(Node *head);
// Node *search_list(Node *head, Data data);
// Node *concat_list(Node *head1, Node *head2);
// Node *reverse_list(Node *head);

int main(void)
{
    Node *head = NULL;
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

Node *insert(Node *head, Node *pre, Data data)
{
    Node *node = (Node *)malloc(sizeof(Node));
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

Node *delete_first(Node *head)
{
    Node *removed;
    if (head == NULL) return NULL;
    removed = head;
    head = removed->link;
    free(removed);
    return head;
}

Node *delete(Node *head, Node *pre)
{
    Node *removed;
    removed = pre->link;
    pre->link = removed->link;
    free(removed);
    return head;
}

/*
void print_list(Node *head)
{
    Node *p;
    for(p = head; p != NULL; p = p->link)
        printf("%d->", p->data);
    printf("NULL \n");
}
*/