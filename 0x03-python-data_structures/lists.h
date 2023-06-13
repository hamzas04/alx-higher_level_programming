#ifndef LISTS_H
#define LISTS_H

#include <stdio.h>
#include <stdlib.h>

/* Definition for singly-linked list */
typedef struct listint_s
{
  int n;
  struct listint_s *next;
} listint_t;

/* Function prototype */
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
