// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from avai_messages:msg/Motors.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "avai_messages/msg/detail/motors__rosidl_typesupport_introspection_c.h"
#include "avai_messages/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "avai_messages/msg/detail/motors__functions.h"
#include "avai_messages/msg/detail/motors__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `motors`
#include "avai_messages/msg/motor.h"
// Member `motors`
#include "avai_messages/msg/detail/motor__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  avai_messages__msg__Motors__init(message_memory);
}

void avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_fini_function(void * message_memory)
{
  avai_messages__msg__Motors__fini(message_memory);
}

size_t avai_messages__msg__Motors__rosidl_typesupport_introspection_c__size_function__Motors__motors(
  const void * untyped_member)
{
  const avai_messages__msg__Motor__Sequence * member =
    (const avai_messages__msg__Motor__Sequence *)(untyped_member);
  return member->size;
}

const void * avai_messages__msg__Motors__rosidl_typesupport_introspection_c__get_const_function__Motors__motors(
  const void * untyped_member, size_t index)
{
  const avai_messages__msg__Motor__Sequence * member =
    (const avai_messages__msg__Motor__Sequence *)(untyped_member);
  return &member->data[index];
}

void * avai_messages__msg__Motors__rosidl_typesupport_introspection_c__get_function__Motors__motors(
  void * untyped_member, size_t index)
{
  avai_messages__msg__Motor__Sequence * member =
    (avai_messages__msg__Motor__Sequence *)(untyped_member);
  return &member->data[index];
}

void avai_messages__msg__Motors__rosidl_typesupport_introspection_c__fetch_function__Motors__motors(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const avai_messages__msg__Motor * item =
    ((const avai_messages__msg__Motor *)
    avai_messages__msg__Motors__rosidl_typesupport_introspection_c__get_const_function__Motors__motors(untyped_member, index));
  avai_messages__msg__Motor * value =
    (avai_messages__msg__Motor *)(untyped_value);
  *value = *item;
}

void avai_messages__msg__Motors__rosidl_typesupport_introspection_c__assign_function__Motors__motors(
  void * untyped_member, size_t index, const void * untyped_value)
{
  avai_messages__msg__Motor * item =
    ((avai_messages__msg__Motor *)
    avai_messages__msg__Motors__rosidl_typesupport_introspection_c__get_function__Motors__motors(untyped_member, index));
  const avai_messages__msg__Motor * value =
    (const avai_messages__msg__Motor *)(untyped_value);
  *item = *value;
}

bool avai_messages__msg__Motors__rosidl_typesupport_introspection_c__resize_function__Motors__motors(
  void * untyped_member, size_t size)
{
  avai_messages__msg__Motor__Sequence * member =
    (avai_messages__msg__Motor__Sequence *)(untyped_member);
  avai_messages__msg__Motor__Sequence__fini(member);
  return avai_messages__msg__Motor__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_message_member_array[2] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages__msg__Motors, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "motors",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages__msg__Motors, motors),  // bytes offset in struct
    NULL,  // default value
    avai_messages__msg__Motors__rosidl_typesupport_introspection_c__size_function__Motors__motors,  // size() function pointer
    avai_messages__msg__Motors__rosidl_typesupport_introspection_c__get_const_function__Motors__motors,  // get_const(index) function pointer
    avai_messages__msg__Motors__rosidl_typesupport_introspection_c__get_function__Motors__motors,  // get(index) function pointer
    avai_messages__msg__Motors__rosidl_typesupport_introspection_c__fetch_function__Motors__motors,  // fetch(index, &value) function pointer
    avai_messages__msg__Motors__rosidl_typesupport_introspection_c__assign_function__Motors__motors,  // assign(index, value) function pointer
    avai_messages__msg__Motors__rosidl_typesupport_introspection_c__resize_function__Motors__motors  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_message_members = {
  "avai_messages__msg",  // message namespace
  "Motors",  // message name
  2,  // number of fields
  sizeof(avai_messages__msg__Motors),
  avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_message_member_array,  // message members
  avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_init_function,  // function to initialize message memory (memory has to be allocated)
  avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_message_type_support_handle = {
  0,
  &avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_avai_messages
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, avai_messages, msg, Motors)() {
  avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, avai_messages, msg, Motor)();
  if (!avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_message_type_support_handle.typesupport_identifier) {
    avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &avai_messages__msg__Motors__rosidl_typesupport_introspection_c__Motors_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
