#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *a)
{
	long int size = PyList_Size(a);
	int i;
	PyListObject *obj = (PyListObject *)a;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
