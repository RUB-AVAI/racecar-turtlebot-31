// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/Motor.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__MOTOR__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__MOTOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/Motor in the package avai_messages.
typedef struct avai_messages__msg__Motor
{
  int64_t position;
  int16_t velocity;
} avai_messages__msg__Motor;

// Struct for a sequence of avai_messages__msg__Motor.
typedef struct avai_messages__msg__Motor__Sequence
{
  avai_messages__msg__Motor * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__Motor__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__MOTOR__STRUCT_H_
