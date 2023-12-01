// generated from rosidl_generator_py/resource/_idl_support.c.em
// with input from avai_messages:msg/VehicleLights.idl
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
#include "avai_messages/msg/detail/vehicle_lights__struct.h"
#include "avai_messages/msg/detail/vehicle_lights__functions.h"


ROSIDL_GENERATOR_C_EXPORT
bool avai_messages__msg__vehicle_lights__convert_from_py(PyObject * _pymsg, void * _ros_message)
{
  // check that the passed message is of the expected Python class
  {
    char full_classname_dest[48];
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
    assert(strncmp("avai_messages.msg._vehicle_lights.VehicleLights", full_classname_dest, 47) == 0);
  }
  avai_messages__msg__VehicleLights * ros_message = _ros_message;
  {  // left_motor
    PyObject * field = PyObject_GetAttrString(_pymsg, "left_motor");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->left_motor = (Py_True == field);
    Py_DECREF(field);
  }
  {  // right_motor
    PyObject * field = PyObject_GetAttrString(_pymsg, "right_motor");
    if (!field) {
      return false;
    }
    assert(PyBool_Check(field));
    ros_message->right_motor = (Py_True == field);
    Py_DECREF(field);
  }

  return true;
}

ROSIDL_GENERATOR_C_EXPORT
PyObject * avai_messages__msg__vehicle_lights__convert_to_py(void * raw_ros_message)
{
  /* NOTE(esteve): Call constructor of VehicleLights */
  PyObject * _pymessage = NULL;
  {
    PyObject * pymessage_module = PyImport_ImportModule("avai_messages.msg._vehicle_lights");
    assert(pymessage_module);
    PyObject * pymessage_class = PyObject_GetAttrString(pymessage_module, "VehicleLights");
    assert(pymessage_class);
    Py_DECREF(pymessage_module);
    _pymessage = PyObject_CallObject(pymessage_class, NULL);
    Py_DECREF(pymessage_class);
    if (!_pymessage) {
      return NULL;
    }
  }
  avai_messages__msg__VehicleLights * ros_message = (avai_messages__msg__VehicleLights *)raw_ros_message;
  {  // left_motor
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->left_motor ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "left_motor", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }
  {  // right_motor
    PyObject * field = NULL;
    field = PyBool_FromLong(ros_message->right_motor ? 1 : 0);
    {
      int rc = PyObject_SetAttrString(_pymessage, "right_motor", field);
      Py_DECREF(field);
      if (rc) {
        return NULL;
      }
    }
  }

  // ownership of _pymessage is transferred to the caller
  return _pymessage;
}
