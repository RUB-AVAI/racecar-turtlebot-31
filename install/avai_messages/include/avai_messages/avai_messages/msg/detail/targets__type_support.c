// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from avai_messages:msg/Targets.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "avai_messages/msg/detail/targets__rosidl_typesupport_introspection_c.h"
#include "avai_messages/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "avai_messages/msg/detail/targets__functions.h"
#include "avai_messages/msg/detail/targets__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  avai_messages__msg__Targets__init(message_memory);
}

void avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_fini_function(void * message_memory)
{
  avai_messages__msg__Targets__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_message_member_array[3] = {
  {
    "x_position",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages__msg__Targets, x_position),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "y_position",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages__msg__Targets, y_position),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "round",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages__msg__Targets, round),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_message_members = {
  "avai_messages__msg",  // message namespace
  "Targets",  // message name
  3,  // number of fields
  sizeof(avai_messages__msg__Targets),
  avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_message_member_array,  // message members
  avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_init_function,  // function to initialize message memory (memory has to be allocated)
  avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_message_type_support_handle = {
  0,
  &avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_avai_messages
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, avai_messages, msg, Targets)() {
  if (!avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_message_type_support_handle.typesupport_identifier) {
    avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &avai_messages__msg__Targets__rosidl_typesupport_introspection_c__Targets_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
