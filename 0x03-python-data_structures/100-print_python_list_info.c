#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Prints basic information about Python lists
 * @p: Pointer to the Python object
 */
void print_python_list_info(PyObject *p)
{
  PyListObject *list = (PyListObject *)p;
  Py_ssize_t size = PyList_Size(p);
  Py_ssize_t allocated = list->allocated;
  Py_ssize_t i;

  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld\n", allocated);

  for (i = 0; i < size; i++)
    {
      PyObject *item = PyList_GetItem(p, i);
      const char *type = Py_TYPE(item)->tp_name;
      printf("Element %ld: %s\n", i, type);
    }
}
