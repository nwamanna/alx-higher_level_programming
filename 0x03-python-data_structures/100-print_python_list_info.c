#include <stdio.h>
#include <Python.h>
/**
*print_python_list_info - prints element in a python list
*@p: parameter
*Return: Void
*/
void print_python_list_info(PyObject *p)
{
	int size, alloc;
	int i;
	PyObject *obj;

	size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}

