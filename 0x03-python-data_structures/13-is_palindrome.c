#include "lists.h"

/**
 * Definition for singly-linked list.
 * struct listint_s {
 * int n;
 * struct listint_s *next;
 * };
 * typedef struct listint_s listint_t;
 */

int is_palindrome(listint_t **head)
{
  if (*head == NULL)
    return 1;

  listint_t *slow = *head;
  listint_t *fast = *head;
  while (fast != NULL && fast->next != NULL)
    {
      slow = slow->next;
      fast = fast->next->next;
    }

  listint_t *prev = NULL;
  listint_t *current = slow;
  listint_t *next;
  while (current != NULL)
    {
      next = current->next;
      current->next = prev;
      prev = current;
      current = next;
    }

  listint_t *left = *head;
  listint_t *right = prev;
  while (right != NULL)
    {
      if (left->n != right->n)
	return 0;
      left = left->next;
      right = right->next;
    }

  return (1);
}
