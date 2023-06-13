#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the list
 *
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
  listint_t *prev = NULL;
  listint_t *current = *head;
  listint_t *next = NULL;

  while (current != NULL)
    {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
    }

  return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Double pointer to the head of the list
 *
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
  listint_t *slow = *head;
  listint_t *fast = *head;
  listint_t *mid = NULL;
  listint_t *second_half = NULL;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  /* Find the middle node using slow and fast pointers */
  while (fast != NULL && fast->next != NULL)
    {
      slow = slow->next;
      fast = fast->next->next;
    }

  /* For odd number of nodes, skip the middle node */
  if (fast != NULL)
    {
      mid = slow;
      slow = slow->next;
    }

  /* Reverse the second half of the list */
  second_half = reverse_list(&slow);

  /* Compare the first and second halves of the list */
  while (second_half != NULL)
    {
      if ((*head)->n != second_half->n)
	return (0);
      *head = (*head)->next;
      second_half = second_half->next;
    }

  if (mid != NULL)
    *head = (*head)->next;

  return (1);
}
