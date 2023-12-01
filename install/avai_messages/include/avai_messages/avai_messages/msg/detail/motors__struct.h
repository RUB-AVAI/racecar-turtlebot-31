// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/Motors.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__MOTORS__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__MOTORS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'motors'
#include "avai_messages/msg/detail/motor__struct.h"

/// Struct defined in msg/Motors in the package avai_messages.
typedef struct avai_messages__msg__Motors
{
  avai_messages__msg__Motor__Sequence motors;
} avai_messages__msg__Motors;

// Struct for a sequence of avai_messages__msg__Motors.
typedef struct avai_messages__msg__Motors__Sequence
{
  avai_messages__msg__Motors * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__Motors__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__MOTORS__STRUCT_H_
