#include <stdlib.h>
#include <stdio.h>	

typedef struct Node
{
	int data;
	struct Node* next;
}Node;

static Node* insert(Node *head, int data)
{
	//Complete this function
	Node* temp;
	Node* new;
	new =(struct Node*)malloc (sizeof(Node));
	new->data=data;
	new->next=NULL;
	if (head==NULL)
		return new;
	else
	{
		temp=head;
		while(temp->next!=NULL)
		temp=temp->next;
		temp->next=new;
		return head;
	}
}

static void display(Node *head)
{
	Node *start=head;
	while(start)
	{
		printf("%d ",start->data);
		start=start->next;
	}
}

int main()
{
	int T,data;
	scanf("%d",&T);
	Node *head=NULL;	
	while(T-->0){
		scanf("%d",&data);
		head=insert(head,data);
    	}
	display(head);
	return 0;
}

