// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from avai_messages:msg/VehicleLights.idl
// generated code does not contain a copyright notice
#include "avai_messages/msg/detail/vehicle_lights__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "avai_messages/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "avai_messages/msg/detail/vehicle_lights__struct.h"
#include "avai_messages/msg/detail/vehicle_lights__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif


// forward declare type support functions


using _VehicleLights__ros_msg_type = avai_messages__msg__VehicleLights;

static bool _VehicleLights__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _VehicleLights__ros_msg_type * ros_message = static_cast<const _VehicleLights__ros_msg_type *>(untyped_ros_message);
  // Field name: left_motor
  {
    cdr << (ros_message->left_motor ? true : false);
  }

  // Field name: right_motor
  {
    cdr << (ros_message->right_motor ? true : false);
  }

  return true;
}

static bool _VehicleLights__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _VehicleLights__ros_msg_type * ros_message = static_cast<_VehicleLights__ros_msg_type *>(untyped_ros_message);
  // Field name: left_motor
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->left_motor = tmp ? true : false;
  }

  // Field name: right_motor
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message->right_motor = tmp ? true : false;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avai_messages
size_t get_serialized_size_avai_messages__msg__VehicleLights(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _VehicleLights__ros_msg_type * ros_message = static_cast<const _VehicleLights__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name left_motor
  {
    size_t item_size = sizeof(ros_message->left_motor);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name right_motor
  {
    size_t item_size = sizeof(ros_message->right_motor);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _VehicleLights__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_avai_messages__msg__VehicleLights(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avai_messages
size_t max_serialized_size_avai_messages__msg__VehicleLights(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;

  // member: left_motor
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }
  // member: right_motor
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint8_t);
  }

  return current_alignment - initial_alignment;
}

static size_t _VehicleLights__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_avai_messages__msg__VehicleLights(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_VehicleLights = {
  "avai_messages::msg",
  "VehicleLights",
  _VehicleLights__cdr_serialize,
  _VehicleLights__cdr_deserialize,
  _VehicleLights__get_serialized_size,
  _VehicleLights__max_serialized_size
};

static rosidl_message_type_support_t _VehicleLights__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_VehicleLights,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, avai_messages, msg, VehicleLights)() {
  return &_VehicleLights__type_support;
}

#if defined(__cplusplus)
}
#endif
