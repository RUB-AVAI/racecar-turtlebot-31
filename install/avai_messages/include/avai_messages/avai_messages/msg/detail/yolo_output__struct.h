// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/YoloOutput.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__YOLO_OUTPUT__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__YOLO_OUTPUT__STRUCT_H_

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
// Member 'bounding_boxes'
#include "avai_messages/msg/detail/bounding_box__struct.h"

/// Struct defined in msg/YoloOutput in the package avai_messages.
typedef struct avai_messages__msg__YoloOutput
{
  std_msgs__msg__Header header;
  avai_messages__msg__BoundingBox__Sequence bounding_boxes;
} avai_messages__msg__YoloOutput;

// Struct for a sequence of avai_messages__msg__YoloOutput.
typedef struct avai_messages__msg__YoloOutput__Sequence
{
  avai_messages__msg__YoloOutput * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__YoloOutput__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__YOLO_OUTPUT__STRUCT_H_
