// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/Target.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__TARGET__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__TARGET__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/Target in the package avai_messages.
typedef struct avai_messages__msg__Target
{
  std_msgs__msg__Header header;
  double x_position;
  double y_position;
  int8_t round;
  double turn_angle;
} avai_messages__msg__Target;

// Struct for a sequence of avai_messages__msg__Target.
typedef struct avai_messages__msg__Target__Sequence
{
  avai_messages__msg__Target * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__Target__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__TARGET__STRUCT_H_
