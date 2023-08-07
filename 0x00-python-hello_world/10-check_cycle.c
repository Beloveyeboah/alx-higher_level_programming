#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in the nodes
 * @list: the parameterto check the cyclce
 * Return: 0 if no cycle found / 1 if found
 */
int check_cycle(listint_t *list)
{
	listint_t *foward = list;
	listint_t *con = list;

	if (list == NULL)
	{
		return (0);
	}
	while (foward && con && con->next)
	{
		foward = foward->next;
		con = con->next->next;

		if (foward == con)
		{
			return (1);
		}
	}
	return (0);
}
