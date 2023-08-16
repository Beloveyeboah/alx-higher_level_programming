#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: python object
 */
void print_python_list_info(PyObject *p)
{
	size_t love, x = 0;
	PyObject *obj;

	love = PyList_Size(p);
	printf("[*] Size of the Python List = %zu\n", love);
	printf("[*] Allocated = %zu\n", ((PyListObject *)p)->allocated);
	while (x < love)
	{
		obj = PyList_GET_ITEM(p, x);
		printf("Element %zu: %s\n", x, Py_TYPE(obj)->tp_name);
		x++;
	}
}
