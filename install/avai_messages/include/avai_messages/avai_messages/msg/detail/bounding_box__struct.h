// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/BoundingBox in the package avai_messages.
typedef struct avai_messages__msg__BoundingBox
{
  double min_x;
  double min_y;
  double max_x;
  double max_y;
  double confidence;
  int16_t cone;
} avai_messages__msg__BoundingBox;

// Struct for a sequence of avai_messages__msg__BoundingBox.
typedef struct avai_messages__msg__BoundingBox__Sequence
{
  avai_messages__msg__BoundingBox * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__BoundingBox__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__STRUCT_H_
