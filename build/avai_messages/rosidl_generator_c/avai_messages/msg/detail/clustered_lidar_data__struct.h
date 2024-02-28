// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from avai_messages:msg/ClusteredLidarData.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__CLUSTERED_LIDAR_DATA__STRUCT_H_
#define AVAI_MESSAGES__MSG__DETAIL__CLUSTERED_LIDAR_DATA__STRUCT_H_

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
// Member 'clusters'
#include "avai_messages/msg/detail/cluster__struct.h"

/// Struct defined in msg/ClusteredLidarData in the package avai_messages.
typedef struct avai_messages__msg__ClusteredLidarData
{
  std_msgs__msg__Header header;
  avai_messages__msg__Cluster__Sequence clusters;
} avai_messages__msg__ClusteredLidarData;

// Struct for a sequence of avai_messages__msg__ClusteredLidarData.
typedef struct avai_messages__msg__ClusteredLidarData__Sequence
{
  avai_messages__msg__ClusteredLidarData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} avai_messages__msg__ClusteredLidarData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__CLUSTERED_LIDAR_DATA__STRUCT_H_
