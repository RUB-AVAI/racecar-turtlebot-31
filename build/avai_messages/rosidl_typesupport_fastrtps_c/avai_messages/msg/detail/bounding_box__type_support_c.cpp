// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from avai_messages:msg/BoundingBox.idl
// generated code does not contain a copyright notice
#include "avai_messages/msg/detail/bounding_box__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "avai_messages/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "avai_messages/msg/detail/bounding_box__struct.h"
#include "avai_messages/msg/detail/bounding_box__functions.h"
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


using _BoundingBox__ros_msg_type = avai_messages__msg__BoundingBox;

static bool _BoundingBox__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _BoundingBox__ros_msg_type * ros_message = static_cast<const _BoundingBox__ros_msg_type *>(untyped_ros_message);
  // Field name: min_x
  {
    cdr << ros_message->min_x;
  }

  // Field name: min_y
  {
    cdr << ros_message->min_y;
  }

  // Field name: max_x
  {
    cdr << ros_message->max_x;
  }

  // Field name: max_y
  {
    cdr << ros_message->max_y;
  }

  // Field name: confidence
  {
    cdr << ros_message->confidence;
  }

  // Field name: cone
  {
    cdr << ros_message->cone;
  }

  return true;
}

static bool _BoundingBox__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _BoundingBox__ros_msg_type * ros_message = static_cast<_BoundingBox__ros_msg_type *>(untyped_ros_message);
  // Field name: min_x
  {
    cdr >> ros_message->min_x;
  }

  // Field name: min_y
  {
    cdr >> ros_message->min_y;
  }

  // Field name: max_x
  {
    cdr >> ros_message->max_x;
  }

  // Field name: max_y
  {
    cdr >> ros_message->max_y;
  }

  // Field name: confidence
  {
    cdr >> ros_message->confidence;
  }

  // Field name: cone
  {
    cdr >> ros_message->cone;
  }

  return true;
}  // NOLINT(readability/fn_size)

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avai_messages
size_t get_serialized_size_avai_messages__msg__BoundingBox(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _BoundingBox__ros_msg_type * ros_message = static_cast<const _BoundingBox__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name min_x
  {
    size_t item_size = sizeof(ros_message->min_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name min_y
  {
    size_t item_size = sizeof(ros_message->min_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name max_x
  {
    size_t item_size = sizeof(ros_message->max_x);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name max_y
  {
    size_t item_size = sizeof(ros_message->max_y);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name confidence
  {
    size_t item_size = sizeof(ros_message->confidence);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name cone
  {
    size_t item_size = sizeof(ros_message->cone);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _BoundingBox__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_avai_messages__msg__BoundingBox(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_avai_messages
size_t max_serialized_size_avai_messages__msg__BoundingBox(
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

  // member: min_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: min_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: max_x
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: max_y
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: confidence
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint64_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint64_t));
  }
  // member: cone
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint16_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint16_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _BoundingBox__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_avai_messages__msg__BoundingBox(
    full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}


static message_type_support_callbacks_t __callbacks_BoundingBox = {
  "avai_messages::msg",
  "BoundingBox",
  _BoundingBox__cdr_serialize,
  _BoundingBox__cdr_deserialize,
  _BoundingBox__get_serialized_size,
  _BoundingBox__max_serialized_size
};

static rosidl_message_type_support_t _BoundingBox__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_BoundingBox,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, avai_messages, msg, BoundingBox)() {
  return &_BoundingBox__type_support;
}

#if defined(__cplusplus)
}
#endif
