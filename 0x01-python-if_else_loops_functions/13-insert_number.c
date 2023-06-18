#include "lists.h"
/**
 * insert_node - Inserts a number
 * @head: A pointer the head
 * @number: The number to insert
 * Return: NULL for fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *odd;

	odd = malloc(sizeof(listint_t));
	if (odd == NULL)
		return (NULL);
	odd->n = number;

	if (node == NULL || node->n >= number)
	{
		odd->next = node;
		*head = odd;
		return (odd);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	odd->next = node->next;
	node->next = odd;

	return (odd);
}
