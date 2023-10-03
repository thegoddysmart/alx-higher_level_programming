#include "lists.h"

/**
 * check_cycle - this checks if a linked list contains a cycle
 * @list: the linked list we are checking
 *
 * Return: 1 if success, 0 if fail
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
