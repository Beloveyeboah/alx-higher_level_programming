#include "python.h"

/**
 * print_python_string - Print details  about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int obj;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	obj = ((PyASCIIObject *)(p))->obj;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", obj);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &obj));
}
