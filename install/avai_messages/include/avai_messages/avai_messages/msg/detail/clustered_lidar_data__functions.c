// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avai_messages:msg/ClusteredLidarData.idl
// generated code does not contain a copyright notice
#include "avai_messages/msg/detail/clustered_lidar_data__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `clusters`
#include "avai_messages/msg/detail/cluster__functions.h"

bool
avai_messages__msg__ClusteredLidarData__init(avai_messages__msg__ClusteredLidarData * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    avai_messages__msg__ClusteredLidarData__fini(msg);
    return false;
  }
  // clusters
  if (!avai_messages__msg__Cluster__Sequence__init(&msg->clusters, 0)) {
    avai_messages__msg__ClusteredLidarData__fini(msg);
    return false;
  }
  return true;
}

void
avai_messages__msg__ClusteredLidarData__fini(avai_messages__msg__ClusteredLidarData * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // clusters
  avai_messages__msg__Cluster__Sequence__fini(&msg->clusters);
}

bool
avai_messages__msg__ClusteredLidarData__are_equal(const avai_messages__msg__ClusteredLidarData * lhs, const avai_messages__msg__ClusteredLidarData * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // clusters
  if (!avai_messages__msg__Cluster__Sequence__are_equal(
      &(lhs->clusters), &(rhs->clusters)))
  {
    return false;
  }
  return true;
}

bool
avai_messages__msg__ClusteredLidarData__copy(
  const avai_messages__msg__ClusteredLidarData * input,
  avai_messages__msg__ClusteredLidarData * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // clusters
  if (!avai_messages__msg__Cluster__Sequence__copy(
      &(input->clusters), &(output->clusters)))
  {
    return false;
  }
  return true;
}

avai_messages__msg__ClusteredLidarData *
avai_messages__msg__ClusteredLidarData__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__ClusteredLidarData * msg = (avai_messages__msg__ClusteredLidarData *)allocator.allocate(sizeof(avai_messages__msg__ClusteredLidarData), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avai_messages__msg__ClusteredLidarData));
  bool success = avai_messages__msg__ClusteredLidarData__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avai_messages__msg__ClusteredLidarData__destroy(avai_messages__msg__ClusteredLidarData * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avai_messages__msg__ClusteredLidarData__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avai_messages__msg__ClusteredLidarData__Sequence__init(avai_messages__msg__ClusteredLidarData__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__ClusteredLidarData * data = NULL;

  if (size) {
    data = (avai_messages__msg__ClusteredLidarData *)allocator.zero_allocate(size, sizeof(avai_messages__msg__ClusteredLidarData), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avai_messages__msg__ClusteredLidarData__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avai_messages__msg__ClusteredLidarData__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
avai_messages__msg__ClusteredLidarData__Sequence__fini(avai_messages__msg__ClusteredLidarData__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      avai_messages__msg__ClusteredLidarData__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

avai_messages__msg__ClusteredLidarData__Sequence *
avai_messages__msg__ClusteredLidarData__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__ClusteredLidarData__Sequence * array = (avai_messages__msg__ClusteredLidarData__Sequence *)allocator.allocate(sizeof(avai_messages__msg__ClusteredLidarData__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avai_messages__msg__ClusteredLidarData__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avai_messages__msg__ClusteredLidarData__Sequence__destroy(avai_messages__msg__ClusteredLidarData__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avai_messages__msg__ClusteredLidarData__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avai_messages__msg__ClusteredLidarData__Sequence__are_equal(const avai_messages__msg__ClusteredLidarData__Sequence * lhs, const avai_messages__msg__ClusteredLidarData__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avai_messages__msg__ClusteredLidarData__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avai_messages__msg__ClusteredLidarData__Sequence__copy(
  const avai_messages__msg__ClusteredLidarData__Sequence * input,
  avai_messages__msg__ClusteredLidarData__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avai_messages__msg__ClusteredLidarData);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    avai_messages__msg__ClusteredLidarData * data =
      (avai_messages__msg__ClusteredLidarData *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avai_messages__msg__ClusteredLidarData__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          avai_messages__msg__ClusteredLidarData__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!avai_messages__msg__ClusteredLidarData__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
