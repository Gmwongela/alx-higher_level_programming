#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"


/**
 * print_dlistint - funtion that prints all the elements of a dlistint_t list
 * @h: The head of the dlistint_t list
 *
 * Return: number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t nodes = 0;

	while (h)
	{
		nodes++;
		printf("%d\n", h->n);
		h = h->next;
	}

	return (nodes);
}
