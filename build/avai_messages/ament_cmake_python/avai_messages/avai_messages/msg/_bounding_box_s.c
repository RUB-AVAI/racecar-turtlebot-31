// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from avai_messages:msg/BoundingBox.idl
// generated code does not contain a copyright notice
#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <stdbool.h>
#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-function"
#endif
#include "numpy/ndarrayobject.h"
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif
#include "rosidl_runtime_c/visibility_control.h"
#include "avai_messages/msg/detail/bounding_box__struct.h"
#include "avai_messages/msg/detail/bounding_box__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool avai_messages__msg__bounding_box__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[44];
    {
      char * class_name = NULL;
      char * module_name = NULL;
      {
        PyObject * class_attr = PyObject_GetAttrString(_pymsg, "__class__");
        if (class_attr) {
          PyObject * name_attr = PyObject_GetAttrString(class_attr, "__name__");
          if (name_attr) {
            class_name = (char *)PyUnicode_1BYTE_DATA(name_attr);
            Py_DECREF(name_attr);
          }
          PyObject * module_attr = PyObject_GetAttrString(class_attr, "__module__");
          if (module_attr) {
            module_name = (char *)PyUnicode_1BYTE_DATA(module_attr);
            Py_DECREF(module_attr);
          }
          Py_DECREF(class_attr);
        }
      }
      if (!class_name || !module_name) {
        return false;
      }
      snprintf(full_classname_dest, sizeof(full_classname_dest), "%s.%s", module_name, class_name);
    }
    assert(strncmp("avai_messages.msg._bounding_box.BoundingBox", full_classname_dest, 43) == 0);
  }
  avai_messages__msg__BoundingBox * ros_message = _ros_message;
  {  // min_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "min_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->min_x = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // min_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "min_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->min_y = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // max_x
    PyObject * field = PyObject_GetAttrString(_pymsg, "max_x");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->max_x = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // max_y
    PyObject * field = PyObject_GetAttrString(_pymsg, "max_y");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->max_y = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // confidence
    PyObject * field = PyObject_GetAttrString(_pymsg, "confidence");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->confidence = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // cone
    PyObject * field = PyObject_GetAttrString(_pymsg, "cone");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->cone = (int16_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * avai_messages__msg__bounding_box__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of BoundingBox */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("avai_messages.msg._bounding_box");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "BoundingBox");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  avai_messages__msg__BoundingBox * ros_message = (avai_messages__msg__BoundingBox *)raw_ros_message;
  {  // min_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->min_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "min_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // min_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->min_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "min_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // max_x
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->max_x);
    {
      int rc = PyObject_SetAttrString(_pymessage, "max_x", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // max_y
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->max_y);
    {
      int rc = PyObject_SetAttrString(_pymessage, "max_y", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // confidence
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->confidence);
    {
      int rc = PyObject_SetAttrString(_pymessage, "confidence", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // cone
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->cone);
    {
      int rc = PyObject_SetAttrString(_pymessage, "cone", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
