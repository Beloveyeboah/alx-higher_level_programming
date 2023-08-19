#include "pie.h"

/**
 * print_python_list - prints list of python
 * @p: the obj
 * Return: obj
 */
void print_python_list(PyObject *p)
{
        Py_ssize_t size;
	Py_ssize_t i;
        const char *item_type; 

	if (!PyList_Check(p))
	{
		printf("Invalid Python List\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject*)p)->allocated);
	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		item_type = item->ob_type->tp_name;
		printf("Element %zd: %s\n", i, item_type);
	}
}

/**
* print_python_bytes - prints the bytes of py
* @p: the pointer
* Return: 0
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size;
	Py_ssize_t max_bytes;
	unsigned char *buffer;
	
	if (!PyBytes_Check(p))
	{
		printf("Invalid Python Bytes\n");
		return;
	}
	size = PyBytes_Size(p);
	max_bytes = 10;
	buffer = (unsigned char *)PyBytes_AsString(p);
	printf("[.] bytes object info\n");
	printf("  [.] Length: %zd\n", size);
	printf("  [.] Bytes: ");
	for (Py_ssize_t i = 0; i < size; i++)
	{
		if (i < max_bytes)
		{
			printf("%02x", buffer[i]);
			if (i != size - 1)
			{
				printf(" ");
			}
		}
	}

printf("\n");
}		
