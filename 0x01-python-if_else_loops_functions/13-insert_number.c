#include"lists.h"
#include<stdio.h>
#include<stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to a pointer to the first node
 * @number: number to insert in the list
 * Return: address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = NULL;
	listint_t *new = NULL;

	temp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (number < temp->n)
	{
		new->next = temp;
		*head = new;
		return (new);
	}
	while (temp->next != NULL && number > temp->next->n)
	{
		temp = temp->next;
	}
	new->next = temp->next;
	temp->next = new;
	return (new);
}


