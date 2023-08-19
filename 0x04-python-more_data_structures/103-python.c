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
=======
void print_python_list(Pyobject *p)
{
        Py_ssize_t size;
        const char *itemtype;
        Pyobject *item;

        if (!Pylist_check(p))
        {
                printf("error: input is not a valid python list.\n");
                return;
        }
        size = Pylist_size(p);
        printf("[*] python list info\n");
        printf("[*] size of the list = %zd\n", size);
        printf("[*] allocated = %zd\n", ((Pylistobject *)p)->allocated);
        for (Py_ssize_t <F9>i = 0; i < size; i++)
        {
                item = Pylist_getitem(p, i);
                itemtype = item->ob_type->tp_name;
                printf("element %zd: %s\n", i, itemtype);
        }
>>>>>>> 17af8bd11539aad0c80b8186e1b49163f737d0c7
}

/**
<<<<<<< HEAD
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
=======
 * print_python_bytes - prints the bytesof py
 * @p: the objesct
 * Return: the obj
 */
void print_python_bytes(Pyobject *p)
{
        Py_ssize_t size;
        Py_ssize_t maxbytes;
        char *bytes;

        if (!Pybytes_check(p))
        {
                printf("error: input is not a valid python bytes object.\n");
                return;
        }
        size = Pybytes_size(p);
        printf("[*] python bytes info\n");
        printf("[*] size of the object = %zd\n", size);
        printf("[*] bytes object contents: ");
        if (size > 0)
        {
                maxbytes = 10;
                bytes = Pybytes_asstring(p);
        }
        for (Py_ssize_t i = 0; i < size && i < maxbytes; i++)
        {
                printf("%02x", bytes[i] & 0xff);
        }
        if (size > maxbytes)
        {
                printf("...");
        }

        printf("\n");
}
>>>>>>> 17af8bd11539aad0c80b8186e1b49163f737d0c7
