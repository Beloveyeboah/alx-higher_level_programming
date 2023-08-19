#include "pie.h"

/**
 * print_python_list - prints list of python
 * @p: the obj
 * Return: obj
 */
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
}




/**
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
