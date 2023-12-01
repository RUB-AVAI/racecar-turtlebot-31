// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avai_messages:msg/VehicleLights.idl
// generated code does not contain a copyright notice
#include "avai_messages/msg/detail/vehicle_lights__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
avai_messages__msg__VehicleLights__init(avai_messages__msg__VehicleLights * msg)
{
  if (!msg) {
    return false;
  }
  // left_motor
  // right_motor
  return true;
}

void
avai_messages__msg__VehicleLights__fini(avai_messages__msg__VehicleLights * msg)
{
  if (!msg) {
    return;
  }
  // left_motor
  // right_motor
}

bool
avai_messages__msg__VehicleLights__are_equal(const avai_messages__msg__VehicleLights * lhs, const avai_messages__msg__VehicleLights * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // left_motor
  if (lhs->left_motor != rhs->left_motor) {
    return false;
  }
  // right_motor
  if (lhs->right_motor != rhs->right_motor) {
    return false;
  }
  return true;
}

bool
avai_messages__msg__VehicleLights__copy(
  const avai_messages__msg__VehicleLights * input,
  avai_messages__msg__VehicleLights * output)
{
  if (!input || !output) {
    return false;
  }
  // left_motor
  output->left_motor = input->left_motor;
  // right_motor
  output->right_motor = input->right_motor;
  return true;
}

avai_messages__msg__VehicleLights *
avai_messages__msg__VehicleLights__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__VehicleLights * msg = (avai_messages__msg__VehicleLights *)allocator.allocate(sizeof(avai_messages__msg__VehicleLights), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avai_messages__msg__VehicleLights));
  bool success = avai_messages__msg__VehicleLights__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avai_messages__msg__VehicleLights__destroy(avai_messages__msg__VehicleLights * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avai_messages__msg__VehicleLights__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avai_messages__msg__VehicleLights__Sequence__init(avai_messages__msg__VehicleLights__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__VehicleLights * data = NULL;

  if (size) {
    data = (avai_messages__msg__VehicleLights *)allocator.zero_allocate(size, sizeof(avai_messages__msg__VehicleLights), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avai_messages__msg__VehicleLights__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avai_messages__msg__VehicleLights__fini(&data[i - 1]);
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
avai_messages__msg__VehicleLights__Sequence__fini(avai_messages__msg__VehicleLights__Sequence * array)
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
      avai_messages__msg__VehicleLights__fini(&array->data[i]);
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

avai_messages__msg__VehicleLights__Sequence *
avai_messages__msg__VehicleLights__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__VehicleLights__Sequence * array = (avai_messages__msg__VehicleLights__Sequence *)allocator.allocate(sizeof(avai_messages__msg__VehicleLights__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avai_messages__msg__VehicleLights__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avai_messages__msg__VehicleLights__Sequence__destroy(avai_messages__msg__VehicleLights__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avai_messages__msg__VehicleLights__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avai_messages__msg__VehicleLights__Sequence__are_equal(const avai_messages__msg__VehicleLights__Sequence * lhs, const avai_messages__msg__VehicleLights__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avai_messages__msg__VehicleLights__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avai_messages__msg__VehicleLights__Sequence__copy(
  const avai_messages__msg__VehicleLights__Sequence * input,
  avai_messages__msg__VehicleLights__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avai_messages__msg__VehicleLights);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    avai_messages__msg__VehicleLights * data =
      (avai_messages__msg__VehicleLights *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avai_messages__msg__VehicleLights__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          avai_messages__msg__VehicleLights__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!avai_messages__msg__VehicleLights__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
