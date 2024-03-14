// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from avai_messages:msg/Target.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "avai_messages/msg/detail/target__rosidl_typesupport_introspection_c.h"
#include "avai_messages/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "avai_messages/msg/detail/target__functions.h"
#include "avai_messages/msg/detail/target__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `x_position`
// Member `y_position`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  avai_messages__msg__Target__init(message_memory);
}

void avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_fini_function(void * message_memory)
{
  avai_messages__msg__Target__fini(message_memory);
}

size_t avai_messages__msg__Target__rosidl_typesupport_introspection_c__size_function__Target__x_position(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_const_function__Target__x_position(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_function__Target__x_position(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void avai_messages__msg__Target__rosidl_typesupport_introspection_c__fetch_function__Target__x_position(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_const_function__Target__x_position(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void avai_messages__msg__Target__rosidl_typesupport_introspection_c__assign_function__Target__x_position(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_function__Target__x_position(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool avai_messages__msg__Target__rosidl_typesupport_introspection_c__resize_function__Target__x_position(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

size_t avai_messages__msg__Target__rosidl_typesupport_introspection_c__size_function__Target__y_position(
  const void * untyped_member)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return member->size;
}

const void * avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_const_function__Target__y_position(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__double__Sequence * member =
    (const rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void * avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_function__Target__y_position(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  return &member->data[index];
}

void avai_messages__msg__Target__rosidl_typesupport_introspection_c__fetch_function__Target__y_position(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const double * item =
    ((const double *)
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_const_function__Target__y_position(untyped_member, index));
  double * value =
    (double *)(untyped_value);
  *value = *item;
}

void avai_messages__msg__Target__rosidl_typesupport_introspection_c__assign_function__Target__y_position(
  void * untyped_member, size_t index, const void * untyped_value)
{
  double * item =
    ((double *)
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_function__Target__y_position(untyped_member, index));
  const double * value =
    (const double *)(untyped_value);
  *item = *value;
}

bool avai_messages__msg__Target__rosidl_typesupport_introspection_c__resize_function__Target__y_position(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__double__Sequence * member =
    (rosidl_runtime_c__double__Sequence *)(untyped_member);
  rosidl_runtime_c__double__Sequence__fini(member);
  return rosidl_runtime_c__double__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_message_member_array[5] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages__msg__Target, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "x_position",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages__msg__Target, x_position),  // bytes offset in struct
    NULL,  // default value
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__size_function__Target__x_position,  // size() function pointer
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_const_function__Target__x_position,  // get_const(index) function pointer
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_function__Target__x_position,  // get(index) function pointer
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__fetch_function__Target__x_position,  // fetch(index, &value) function pointer
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__assign_function__Target__x_position,  // assign(index, value) function pointer
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__resize_function__Target__x_position  // resize(index) function pointer
  },
  {
    "y_position",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages__msg__Target, y_position),  // bytes offset in struct
    NULL,  // default value
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__size_function__Target__y_position,  // size() function pointer
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_const_function__Target__y_position,  // get_const(index) function pointer
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__get_function__Target__y_position,  // get(index) function pointer
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__fetch_function__Target__y_position,  // fetch(index, &value) function pointer
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__assign_function__Target__y_position,  // assign(index, value) function pointer
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__resize_function__Target__y_position  // resize(index) function pointer
  },
  {
    "round",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages__msg__Target, round),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "turn_angle",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages__msg__Target, turn_angle),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_message_members = {
  "avai_messages__msg",  // message namespace
  "Target",  // message name
  5,  // number of fields
  sizeof(avai_messages__msg__Target),
  avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_message_member_array,  // message members
  avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_init_function,  // function to initialize message memory (memory has to be allocated)
  avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_message_type_support_handle = {
  0,
  &avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_avai_messages
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, avai_messages, msg, Target)() {
  avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_message_type_support_handle.typesupport_identifier) {
    avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &avai_messages__msg__Target__rosidl_typesupport_introspection_c__Target_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
