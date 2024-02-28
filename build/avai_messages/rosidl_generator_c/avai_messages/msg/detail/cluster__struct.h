// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/Cluster.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__CLUSTER__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__CLUSTER__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'x_positions'
// Member 'y_positions'
#include "rosidl_runtime_c/primitives_sequence.h"

/// Struct defined in msg/Cluster in the package avai_messages.
typedef struct avai_messages__msg__Cluster
{
  rosidl_runtime_c__double__Sequence x_positions;
  rosidl_runtime_c__double__Sequence y_positions;
  int16_t label;
} avai_messages__msg__Cluster;

// Struct for a sequence of avai_messages__msg__Cluster.
typedef struct avai_messages__msg__Cluster__Sequence
{
  avai_messages__msg__Cluster * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__Cluster__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__CLUSTER__STRUCT_H_
