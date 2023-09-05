<<<<<<< HEAD
#include "Python.h"

/**
 * print_python_string - Prints details about Python strings.
 * @p: A PyObject string object.
 */

void print_python_string(PyObject *p)
{
	long int length;
=======
#include "python.h"

/**
 * print_python_string - Print details  about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int obj;
>>>>>>> 855a08f1d3ce28cb797137cc9521ea5082ec3822

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

<<<<<<< HEAD
	length = ((PyASCIIObject *)(p))->length;
=======
	obj = ((PyASCIIObject *)(p))->obj;
>>>>>>> 855a08f1d3ce28cb797137cc9521ea5082ec3822

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
<<<<<<< HEAD
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
=======
	printf("  length: %ld\n", obj);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &obj));
>>>>>>> 855a08f1d3ce28cb797137cc9521ea5082ec3822
}
