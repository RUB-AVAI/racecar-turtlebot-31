// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/VehicleLights.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/VehicleLights in the package avai_messages.
typedef struct avai_messages__msg__VehicleLights
{
  bool left_motor;
  bool right_motor;
} avai_messages__msg__VehicleLights;

// Struct for a sequence of avai_messages__msg__VehicleLights.
typedef struct avai_messages__msg__VehicleLights__Sequence
{
  avai_messages__msg__VehicleLights * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__VehicleLights__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__STRUCT_H_
