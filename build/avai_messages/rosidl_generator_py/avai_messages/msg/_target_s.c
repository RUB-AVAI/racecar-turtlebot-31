// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from avai_messages:msg/Target.idl
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
#include "avai_messages/msg/detail/target__struct.h"
#include "avai_messages/msg/detail/target__functions.h"

ROSIDL_GENERATOR_C_IMPORT
bool std_msgs__msg__header__convert_from_py(PyObject * _pymsg, void * _ros_message);
ROSIDL_GENERATOR_C_IMPORT
PyObject * std_msgs__msg__header__convert_to_py(void * raw_ros_message);

ROSIDL_GENERATOR_C_EXPORT
bool avai_messages__msg__target__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[33];
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
    assert(strncmp("avai_messages.msg._target.Target", full_classname_dest, 32) == 0);
  }
  avai_messages__msg__Target * ros_message = _ros_message;
  {  // header
    PyObject * field = PyObject_GetAttrString(_pymsg, "header");
    if (!field) {
      return false;
    }
    if (!std_msgs__msg__header__convert_from_py(field, &ros_message->header)) {
      Py_DECREF(field);
      return false;
    }
    Py_DECREF(field);
  }
  {  // x_position
    PyObject * field = PyObject_GetAttrString(_pymsg, "x_position");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->x_position = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // y_position
    PyObject * field = PyObject_GetAttrString(_pymsg, "y_position");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->y_position = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }
  {  // round
    PyObject * field = PyObject_GetAttrString(_pymsg, "round");
    if (!field) {
      return false;
    }
    assert(PyLong_Check(field));
    ros_message->round = (int8_t)PyLong_AsLong(field);
    Py_DECREF(field);
  }
  {  // turn_angle
    PyObject * field = PyObject_GetAttrString(_pymsg, "turn_angle");
    if (!field) {
      return false;
    }
    assert(PyFloat_Check(field));
    ros_message->turn_angle = PyFloat_AS_DOUBLE(field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * avai_messages__msg__target__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of Target */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("avai_messages.msg._target");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "Target");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  avai_messages__msg__Target * ros_message = (avai_messages__msg__Target *)raw_ros_message;
  {  // header
    PyObject * field = NULL;
    field = std_msgs__msg__header__convert_to_py(&ros_message->header);
    if (!field) {
      return NULL;
    }
    {
      int rc = PyObject_SetAttrString(_pymessage, "header", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // x_position
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->x_position);
    {
      int rc = PyObject_SetAttrString(_pymessage, "x_position", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // y_position
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->y_position);
    {
      int rc = PyObject_SetAttrString(_pymessage, "y_position", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // round
    PyObject * field = NULL;
    field = PyLong_FromLong(ros_message->round);
    {
      int rc = PyObject_SetAttrString(_pymessage, "round", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // turn_angle
    PyObject * field = NULL;
    field = PyFloat_FromDouble(ros_message->turn_angle);
    {
      int rc = PyObject_SetAttrString(_pymessage, "turn_angle", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
