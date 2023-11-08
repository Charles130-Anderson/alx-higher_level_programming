#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
/**
 * print_python_list - prints information about a Python list
 * @p: the Python list to print information about
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	if (!PyList_Check(p))
	{
		printf("Not a Python list\n");
		return;
	}

	size = PyList_Size(p);
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
	printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
/**
 * print_python_bytes - prints information about a Python bytes object
 * @p: the Python bytes object to print information about
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %.*s\n", (int)size, PyBytes_AS_STRING(p));
	printf("  first %ld bytes: ", size > 10 ? 10 : size);

	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
	}
	printf("\n");
}
