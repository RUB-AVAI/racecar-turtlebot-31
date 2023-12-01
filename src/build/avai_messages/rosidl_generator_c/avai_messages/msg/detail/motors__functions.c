// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avai_messages:msg/Motors.idl
// generated code does not contain a copyright notice
#include "avai_messages/msg/detail/motors__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `motors`
#include "avai_messages/msg/detail/motor__functions.h"

bool
avai_messages__msg__Motors__init(avai_messages__msg__Motors * msg)
{
  if (!msg) {
    return false;
  }
  // motors
  if (!avai_messages__msg__Motor__Sequence__init(&msg->motors, 0)) {
    avai_messages__msg__Motors__fini(msg);
    return false;
  }
  return true;
}

void
avai_messages__msg__Motors__fini(avai_messages__msg__Motors * msg)
{
  if (!msg) {
    return;
  }
  // motors
  avai_messages__msg__Motor__Sequence__fini(&msg->motors);
}

bool
avai_messages__msg__Motors__are_equal(const avai_messages__msg__Motors * lhs, const avai_messages__msg__Motors * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // motors
  if (!avai_messages__msg__Motor__Sequence__are_equal(
      &(lhs->motors), &(rhs->motors)))
  {
    return false;
  }
  return true;
}

bool
avai_messages__msg__Motors__copy(
  const avai_messages__msg__Motors * input,
  avai_messages__msg__Motors * output)
{
  if (!input || !output) {
    return false;
  }
  // motors
  if (!avai_messages__msg__Motor__Sequence__copy(
      &(input->motors), &(output->motors)))
  {
    return false;
  }
  return true;
}

avai_messages__msg__Motors *
avai_messages__msg__Motors__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Motors * msg = (avai_messages__msg__Motors *)allocator.allocate(sizeof(avai_messages__msg__Motors), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avai_messages__msg__Motors));
  bool success = avai_messages__msg__Motors__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avai_messages__msg__Motors__destroy(avai_messages__msg__Motors * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avai_messages__msg__Motors__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avai_messages__msg__Motors__Sequence__init(avai_messages__msg__Motors__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Motors * data = NULL;

  if (size) {
    data = (avai_messages__msg__Motors *)allocator.zero_allocate(size, sizeof(avai_messages__msg__Motors), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avai_messages__msg__Motors__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avai_messages__msg__Motors__fini(&data[i - 1]);
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
avai_messages__msg__Motors__Sequence__fini(avai_messages__msg__Motors__Sequence * array)
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
      avai_messages__msg__Motors__fini(&array->data[i]);
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

avai_messages__msg__Motors__Sequence *
avai_messages__msg__Motors__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Motors__Sequence * array = (avai_messages__msg__Motors__Sequence *)allocator.allocate(sizeof(avai_messages__msg__Motors__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avai_messages__msg__Motors__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avai_messages__msg__Motors__Sequence__destroy(avai_messages__msg__Motors__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avai_messages__msg__Motors__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avai_messages__msg__Motors__Sequence__are_equal(const avai_messages__msg__Motors__Sequence * lhs, const avai_messages__msg__Motors__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avai_messages__msg__Motors__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avai_messages__msg__Motors__Sequence__copy(
  const avai_messages__msg__Motors__Sequence * input,
  avai_messages__msg__Motors__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avai_messages__msg__Motors);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    avai_messages__msg__Motors * data =
      (avai_messages__msg__Motors *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avai_messages__msg__Motors__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          avai_messages__msg__Motors__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!avai_messages__msg__Motors__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
