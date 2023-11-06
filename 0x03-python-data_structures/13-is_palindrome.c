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
	listint_t *slow, *fast, *prev;

	slow = *head;
	fast = (*head)->next;

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	slow = slow->next;
	fast = prev;

	while (slow != NULL && fast != NULL)
	{
		if (slow->n != fast->n)
		{
			return (0);
		}
		slow = slow->next;
		fast = fast->next;
	}

	return (1);
}
