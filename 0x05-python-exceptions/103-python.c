#include <Python.h>

/**
 * print_python_list - Prints information about a Python list
 * @p: A pointer to the Python list object
 *
 * This function checks if the Python object is a list. If it is,
 * it prints the size of the list and the type of each element in the list.
 * If the Python object is not a list, it prints an error message.
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (Py_ssize_t i = 0; i < PyList_Size(p); i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}
/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A pointer to the Python bytes object
 *
 * This function checks if the Python object is a bytes object. If it is,
 * prints size of the bytes and the first 10 bytes of the bytes object.
 * If the Python object is not a bytes object, it prints an error message.
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("[.] bytes object info\n");
	printf(" size: %ld\n", PyBytes_Size(p));
	printf(" trying string: %s\n", PyUnicode_AsUTF8(p));
	printf(" first %ld bytes: ", PyBytes_Size(p) < 10 ? PyBytes_Size(p) : 10);

	for (Py_ssize_t i = 0; i < PyBytes_Size(p) && i < 10; i++)
	{
		printf("%02x ", ((char *)PyBytes_AsString(p))[i]);
	}

	printf("\n");
}
/**
 * print_python_float - Prints information about a Python float object
 * @p: A pointer to the Python float object
 *
 * This function checks if the Python object is a float object. If it is,
 * prints the value of the float object
 * If the Python object is not a float object,
 * it prints an error message.
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n");
	printf(" value: %.15g\n", PyFloat_AsDouble(p));
}
