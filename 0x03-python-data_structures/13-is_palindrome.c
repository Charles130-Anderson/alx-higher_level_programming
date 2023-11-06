#include <stdio.h>
#include <stdlib.h>
#include "lists.h"


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev, *next, *current;

	slow = *head;
	fast = (*head)->next;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
		prev->next = NULL;
	}

	prev = NULL;
	current = slow;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	while (prev != NULL)
	{
		if (prev->n != (*head)->n)
		{
			return (0);
		}
		prev = prev->next;
		*head = (*head)->next;
	}

	return (1);
}
