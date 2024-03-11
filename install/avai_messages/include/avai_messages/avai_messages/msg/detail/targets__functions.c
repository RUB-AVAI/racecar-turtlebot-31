// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avai_messages:msg/Targets.idl
// generated code does not contain a copyright notice
#include "avai_messages/msg/detail/targets__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
avai_messages__msg__Targets__init(avai_messages__msg__Targets * msg)
{
  if (!msg) {
    return false;
  }
  // x_position
  // y_position
  // round
  return true;
}

void
avai_messages__msg__Targets__fini(avai_messages__msg__Targets * msg)
{
  if (!msg) {
    return;
  }
  // x_position
  // y_position
  // round
}

bool
avai_messages__msg__Targets__are_equal(const avai_messages__msg__Targets * lhs, const avai_messages__msg__Targets * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // x_position
  if (lhs->x_position != rhs->x_position) {
    return false;
  }
  // y_position
  if (lhs->y_position != rhs->y_position) {
    return false;
  }
  // round
  if (lhs->round != rhs->round) {
    return false;
  }
  return true;
}

bool
avai_messages__msg__Targets__copy(
  const avai_messages__msg__Targets * input,
  avai_messages__msg__Targets * output)
{
  if (!input || !output) {
    return false;
  }
  // x_position
  output->x_position = input->x_position;
  // y_position
  output->y_position = input->y_position;
  // round
  output->round = input->round;
  return true;
}

avai_messages__msg__Targets *
avai_messages__msg__Targets__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Targets * msg = (avai_messages__msg__Targets *)allocator.allocate(sizeof(avai_messages__msg__Targets), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avai_messages__msg__Targets));
  bool success = avai_messages__msg__Targets__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avai_messages__msg__Targets__destroy(avai_messages__msg__Targets * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avai_messages__msg__Targets__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avai_messages__msg__Targets__Sequence__init(avai_messages__msg__Targets__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Targets * data = NULL;

  if (size) {
    data = (avai_messages__msg__Targets *)allocator.zero_allocate(size, sizeof(avai_messages__msg__Targets), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avai_messages__msg__Targets__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avai_messages__msg__Targets__fini(&data[i - 1]);
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
avai_messages__msg__Targets__Sequence__fini(avai_messages__msg__Targets__Sequence * array)
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
      avai_messages__msg__Targets__fini(&array->data[i]);
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

avai_messages__msg__Targets__Sequence *
avai_messages__msg__Targets__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Targets__Sequence * array = (avai_messages__msg__Targets__Sequence *)allocator.allocate(sizeof(avai_messages__msg__Targets__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avai_messages__msg__Targets__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avai_messages__msg__Targets__Sequence__destroy(avai_messages__msg__Targets__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avai_messages__msg__Targets__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avai_messages__msg__Targets__Sequence__are_equal(const avai_messages__msg__Targets__Sequence * lhs, const avai_messages__msg__Targets__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avai_messages__msg__Targets__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avai_messages__msg__Targets__Sequence__copy(
  const avai_messages__msg__Targets__Sequence * input,
  avai_messages__msg__Targets__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avai_messages__msg__Targets);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    avai_messages__msg__Targets * data =
      (avai_messages__msg__Targets *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avai_messages__msg__Targets__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          avai_messages__msg__Targets__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!avai_messages__msg__Targets__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
