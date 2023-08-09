#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * listint_t *insert_node - function inser numbers
 * @head: the node
 * @number: the number to be inserted
 * Return: 0
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *star;

	star = malloc(sizeof(listint_t));
	if (star == NULL)
	{
		return (NULL);
	}
	star->n = number;
	if (node == NULL || node->n >= number)
	{
		star->next = node;
		*head = star;
		return (star);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	star->next = node->next;
	node->next = star;

	return (star);
}
