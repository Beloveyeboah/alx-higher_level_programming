#include "pie.h"

/**
 * print_python_list - prints list of python
 * @p: the obj
 * Return: obj
 */
void print_python_list(pyobject *p)
{
        py_ssize_t size;
        const char *itemtype;
        pyobject *item;

        if (!pylist_check(p))
        {
                printf("error: input is not a valid python list.\n");
                return;
        }
        size = pylist_size(p);
        printf("[*] python list info\n");
        printf("[*] size of the list = %zd\n", size);
        printf("[*] allocated = %zd\n", ((pylistobject *)p)->allocated);
        for (py_ssize_t i = 0; i < size; i++)
        {
                item = pylist_getitem(p, i);
                itemtype = item->ob_type->tp_name;
                printf("element %zd: %s\n", i, itemtype);
        }
}




/**
 * print_python_bytes - prints the bytesof py
 * @p: the objesct
 * Return: the obj
 */
void print_python_bytes(pyobject *p)
{
        py_ssize_t size;
        py_ssize_t maxbytes;
        char *bytes;

        if (!pybytes_check(p))
        {
                printf("error: input is not a valid python bytes object.\n");
                return;
        }
        size = pybytes_size(p);
        printf("[*] python bytes info\n");
        printf("[*] size of the object = %zd\n", size);
        printf("[*] bytes object contents: ");
        if (size > 0)
        {
                maxbytes = 10;
                bytes = pybytes_asstring(p);
        }
        for (py_ssize_t i = 0; i < size && i < maxbytes; i++)
        {
                printf("%02x", bytes[i] & 0xff);
        }
        if (size > maxbytes)
        {
                printf("...");
        }
        printf("\n");
}
