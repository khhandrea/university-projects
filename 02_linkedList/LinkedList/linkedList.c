#include <stdio.h>
#include <stdlib.h>

typedef int Data;
typedef struct Node {
    Data data;
    struct Node *link;
} Node;

Node *insert_first(Node *head, Data data);
Node *insert(Node *head, Node *pre, Data data);
Node *delete_first(Node *head);
Node *delete(Node *head, Node *pre);
void print_list(Node *head);
Node *search_list(Node *head, Data data);
Node *concat_list(Node *head1, Node *head2);
Node *reverse_list(Node **head);

int main(void)
{
    Node *head = NULL;
    int i;

    head = insert_first(head, 1); print_list(head);
    head = insert_first(head, 2); print_list(head);
    head = insert_first(head, 3); print_list(head);
    head = insert_first(head, 4); print_list(head);
    head = reverse_list(&head); print_list(head);
    // printf("%d\n", search_list(head, 6) != NULL);
    head = delete_first(head); print_list(head);
    head = delete_first(head); print_list(head);
    head = delete_first(head); print_list(head);
    head = delete_first(head); print_list(head);
    return 0;
}

Node *insert_first(Node *head, Data data)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->data = data;
    node->link = head;
    return head = node;
}

Node *insert(Node *head, Node *pre, Data data)
{
    Node *node = (Node *)malloc(sizeof(Node));
    node->data = data;
    node->link = pre->link;
    pre->link = node;
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

void print_list(Node *head)
{
    Node *p;
    for(p = head; p != NULL; p = p->link)
        printf("%d->", p->data);
    printf("NULL \n");
}

Node* search_list(Node *head, Data data)
{
    Node *p;
    for(p = head; p != NULL; p = p->link)
        if (p->data == data)
            return p;
    return NULL;
}

Node *concat_list(Node *head1, Node *head2)
{
    Node *p;
    for(p = head1; p->link != NULL; p = p->link);
    p->link = head2;
}

Node *reverse_list(Node **head)
{
    Node *p, *q, *r;
    p = NULL;
    q = *head;
    r = (*head)->link;
    for(; r != NULL; r = r->link)
    {
        q->link = p;
        p = q;
        q = r;        
    }
    q->link = p;
    *head = q;
    return *head;
}