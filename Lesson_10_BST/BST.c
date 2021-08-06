#include <stdio.h>
#include <stdlib.h>

typedef int TreeData;
typedef struct Node {
    TreeData data;
    struct Node *parent;
    struct Node *left;
    struct Node *right;
} Node;

typedef Node* QueueData;
typedef struct QueueNode {
    QueueData data;
    struct QueueNode *link;
} QueueNode;

typedef struct Queue {
    QueueNode *front;
    QueueNode *rear;
} Queue;

Node *init_tree();
void *print_tree_inorder(Node *root);
void *print_tree_preorder(Node *root);
void *print_tree_postorder(Node *root);
void *print_tree_levelorder(Node *root);

void init_queue(Queue *queue);
char is_empty(Queue *queue);
void enqueue(Queue *queue, QueueData data);
QueueData dequeue(Queue *queue);


int main(void)
{
    Node *root = init_tree(0);
    root->left = init_tree(1);
    root->right = init_tree(2);
    root->left->left = init_tree(3);
    root->left->right = init_tree(4);
    root->right->right = init_tree(5);
    root->left->left->left = init_tree(6);
    root->left->left->right = init_tree(7);
    root->right->right->left = init_tree(8);
    root->right->right->right = init_tree(9);
    
    print_tree_preorder(root);
	printf("\n");
    print_tree_inorder(root);
	printf("\n");
	print_tree_postorder(root);
	printf("\n");
    print_tree_levelorder(root);
	printf("\n");

    return 0;
}

Node *init_tree(TreeData data)
{
	Node *node = (Node *)calloc(1, sizeof(Node));
	node->data = data;
	return node;
}

void *print_tree_inorder(Node *root)
{
	if(root->left) print_tree_inorder(root->left);
	printf("%d ", root->data);
	if(root->right) print_tree_inorder(root->right);
}

void *print_tree_preorder(Node *root)
{
	printf("%d ", root->data);
	if(root->left) print_tree_preorder(root->left);
	if(root->right) print_tree_preorder(root->right);
}

void *print_tree_postorder(Node *root)
{
	if(root->left) print_tree_postorder(root->left);
	if(root->right) print_tree_postorder(root->right);	
	printf("%d ", root->data);
}

void *print_tree_levelorder(Node *root)
{
	Queue *queue;
	Node *temp;
	
	init_queue(queue);
	enqueue(queue, root);
	while(!is_empty(queue))
	{
		temp = dequeue(queue);
		printf("%d ", temp->data);
		if(temp->left) enqueue(queue, temp->left);
		if(temp->right) enqueue(queue, temp->right);
	}
}

void init_queue(Queue *queue)
{
    queue->front = NULL;
    queue->rear = NULL;
}

char is_empty(Queue *queue)
{
    return (queue->front == NULL);
}

void enqueue(Queue *queue, QueueData data)
{
    QueueNode *temp = (QueueNode *)malloc(sizeof(QueueNode));
    temp->data = data;
    temp->link = NULL;
    if (is_empty(queue))
    {
        queue->front = temp;
        queue->rear = temp;
    }
    else
    {
        queue->rear->link = temp;
        queue->rear = temp;
    }
}

QueueData dequeue(Queue *queue)
{
    QueueNode *temp = queue->front;
    Node *data = temp->data;
    queue->front = queue->front->link;
    if (queue->front == NULL)
        queue->rear = NULL;
    free(temp);
    return data;
}
