// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/Vector3Sensor.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__VECTOR3_SENSOR__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__VECTOR3_SENSOR__STRUCT_H_

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
// Member 'data'
#include "geometry_msgs/msg/detail/vector3__struct.h"

/// Struct defined in msg/Vector3Sensor in the package avai_messages.
typedef struct avai_messages__msg__Vector3Sensor
{
  std_msgs__msg__Header header;
  geometry_msgs__msg__Vector3 data;
  int32_t update_time;
} avai_messages__msg__Vector3Sensor;

// Struct for a sequence of avai_messages__msg__Vector3Sensor.
typedef struct avai_messages__msg__Vector3Sensor__Sequence
{
  avai_messages__msg__Vector3Sensor * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__Vector3Sensor__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__VECTOR3_SENSOR__STRUCT_H_
