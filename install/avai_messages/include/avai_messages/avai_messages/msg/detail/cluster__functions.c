// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avai_messages:msg/Cluster.idl
// generated code does not contain a copyright notice
#include "avai_messages/msg/detail/cluster__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `x_positions`
// Member `y_positions`
// Member `angles`
// Member `ranges`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
avai_messages__msg__Cluster__init(avai_messages__msg__Cluster * msg)
{
  if (!msg) {
    return false;
  }
  // x_positions
  if (!rosidl_runtime_c__double__Sequence__init(&msg->x_positions, 0)) {
    avai_messages__msg__Cluster__fini(msg);
    return false;
  }
  // y_positions
  if (!rosidl_runtime_c__double__Sequence__init(&msg->y_positions, 0)) {
    avai_messages__msg__Cluster__fini(msg);
    return false;
  }
  // angles
  if (!rosidl_runtime_c__int16__Sequence__init(&msg->angles, 0)) {
    avai_messages__msg__Cluster__fini(msg);
    return false;
  }
  // ranges
  if (!rosidl_runtime_c__double__Sequence__init(&msg->ranges, 0)) {
    avai_messages__msg__Cluster__fini(msg);
    return false;
  }
  // label
  return true;
}

void
avai_messages__msg__Cluster__fini(avai_messages__msg__Cluster * msg)
{
  if (!msg) {
    return;
  }
  // x_positions
  rosidl_runtime_c__double__Sequence__fini(&msg->x_positions);
  // y_positions
  rosidl_runtime_c__double__Sequence__fini(&msg->y_positions);
  // angles
  rosidl_runtime_c__int16__Sequence__fini(&msg->angles);
  // ranges
  rosidl_runtime_c__double__Sequence__fini(&msg->ranges);
  // label
}

bool
avai_messages__msg__Cluster__are_equal(const avai_messages__msg__Cluster * lhs, const avai_messages__msg__Cluster * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // x_positions
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->x_positions), &(rhs->x_positions)))
  {
    return false;
  }
  // y_positions
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->y_positions), &(rhs->y_positions)))
  {
    return false;
  }
  // angles
  if (!rosidl_runtime_c__int16__Sequence__are_equal(
      &(lhs->angles), &(rhs->angles)))
  {
    return false;
  }
  // ranges
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->ranges), &(rhs->ranges)))
  {
    return false;
  }
  // label
  if (lhs->label != rhs->label) {
    return false;
  }
  return true;
}

bool
avai_messages__msg__Cluster__copy(
  const avai_messages__msg__Cluster * input,
  avai_messages__msg__Cluster * output)
{
  if (!input || !output) {
    return false;
  }
  // x_positions
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->x_positions), &(output->x_positions)))
  {
    return false;
  }
  // y_positions
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->y_positions), &(output->y_positions)))
  {
    return false;
  }
  // angles
  if (!rosidl_runtime_c__int16__Sequence__copy(
      &(input->angles), &(output->angles)))
  {
    return false;
  }
  // ranges
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->ranges), &(output->ranges)))
  {
    return false;
  }
  // label
  output->label = input->label;
  return true;
}

avai_messages__msg__Cluster *
avai_messages__msg__Cluster__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Cluster * msg = (avai_messages__msg__Cluster *)allocator.allocate(sizeof(avai_messages__msg__Cluster), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avai_messages__msg__Cluster));
  bool success = avai_messages__msg__Cluster__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avai_messages__msg__Cluster__destroy(avai_messages__msg__Cluster * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avai_messages__msg__Cluster__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avai_messages__msg__Cluster__Sequence__init(avai_messages__msg__Cluster__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Cluster * data = NULL;

  if (size) {
    data = (avai_messages__msg__Cluster *)allocator.zero_allocate(size, sizeof(avai_messages__msg__Cluster), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avai_messages__msg__Cluster__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avai_messages__msg__Cluster__fini(&data[i - 1]);
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
avai_messages__msg__Cluster__Sequence__fini(avai_messages__msg__Cluster__Sequence * array)
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
      avai_messages__msg__Cluster__fini(&array->data[i]);
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

avai_messages__msg__Cluster__Sequence *
avai_messages__msg__Cluster__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Cluster__Sequence * array = (avai_messages__msg__Cluster__Sequence *)allocator.allocate(sizeof(avai_messages__msg__Cluster__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avai_messages__msg__Cluster__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avai_messages__msg__Cluster__Sequence__destroy(avai_messages__msg__Cluster__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avai_messages__msg__Cluster__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avai_messages__msg__Cluster__Sequence__are_equal(const avai_messages__msg__Cluster__Sequence * lhs, const avai_messages__msg__Cluster__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avai_messages__msg__Cluster__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avai_messages__msg__Cluster__Sequence__copy(
  const avai_messages__msg__Cluster__Sequence * input,
  avai_messages__msg__Cluster__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avai_messages__msg__Cluster);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    avai_messages__msg__Cluster * data =
      (avai_messages__msg__Cluster *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avai_messages__msg__Cluster__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          avai_messages__msg__Cluster__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!avai_messages__msg__Cluster__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
