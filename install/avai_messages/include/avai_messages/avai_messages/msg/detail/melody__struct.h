// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/Melody.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__MELODY__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__MELODY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'pitch'
// Member 'duration'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/Melody in the package avai_messages.
typedef struct avai_messages__msg__Melody
{
  uint8_t length;
  rosidl_runtime_c__uint16__Sequence pitch;
  rosidl_runtime_c__uint16__Sequence duration;
} avai_messages__msg__Melody;

// Struct for a sequence of avai_messages__msg__Melody.
typedef struct avai_messages__msg__Melody__Sequence
{
  avai_messages__msg__Melody * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__Melody__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__MELODY__STRUCT_H_
