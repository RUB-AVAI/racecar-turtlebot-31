// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/Cones.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__CONES__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__CONES__STRUCT_H_

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
// Member 'cones'
#include "avai_messages/msg/detail/cone__struct.h"

/// Struct defined in msg/Cones in the package avai_messages.
typedef struct avai_messages__msg__Cones
{
  std_msgs__msg__Header header;
  avai_messages__msg__Cone__Sequence cones;
} avai_messages__msg__Cones;

// Struct for a sequence of avai_messages__msg__Cones.
typedef struct avai_messages__msg__Cones__Sequence
{
  avai_messages__msg__Cones * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__Cones__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__CONES__STRUCT_H_
