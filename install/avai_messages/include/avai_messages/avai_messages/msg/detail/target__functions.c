// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from avai_messages:msg/Target.idl
// generated code does not contain a copyright notice
#include "avai_messages/msg/detail/target__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `x_position`
// Member `y_position`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
avai_messages__msg__Target__init(avai_messages__msg__Target * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    avai_messages__msg__Target__fini(msg);
    return false;
  }
  // x_position
  if (!rosidl_runtime_c__double__Sequence__init(&msg->x_position, 0)) {
    avai_messages__msg__Target__fini(msg);
    return false;
  }
  // y_position
  if (!rosidl_runtime_c__double__Sequence__init(&msg->y_position, 0)) {
    avai_messages__msg__Target__fini(msg);
    return false;
  }
  // round
  // turn_angle
  return true;
}

void
avai_messages__msg__Target__fini(avai_messages__msg__Target * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // x_position
  rosidl_runtime_c__double__Sequence__fini(&msg->x_position);
  // y_position
  rosidl_runtime_c__double__Sequence__fini(&msg->y_position);
  // round
  // turn_angle
}

bool
avai_messages__msg__Target__are_equal(const avai_messages__msg__Target * lhs, const avai_messages__msg__Target * rhs)
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
  // x_position
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->x_position), &(rhs->x_position)))
  {
    return false;
  }
  // y_position
  if (!rosidl_runtime_c__double__Sequence__are_equal(
      &(lhs->y_position), &(rhs->y_position)))
  {
    return false;
  }
  // round
  if (lhs->round != rhs->round) {
    return false;
  }
  // turn_angle
  if (lhs->turn_angle != rhs->turn_angle) {
    return false;
  }
  return true;
}

bool
avai_messages__msg__Target__copy(
  const avai_messages__msg__Target * input,
  avai_messages__msg__Target * output)
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
  // x_position
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->x_position), &(output->x_position)))
  {
    return false;
  }
  // y_position
  if (!rosidl_runtime_c__double__Sequence__copy(
      &(input->y_position), &(output->y_position)))
  {
    return false;
  }
  // round
  output->round = input->round;
  // turn_angle
  output->turn_angle = input->turn_angle;
  return true;
}

avai_messages__msg__Target *
avai_messages__msg__Target__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Target * msg = (avai_messages__msg__Target *)allocator.allocate(sizeof(avai_messages__msg__Target), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(avai_messages__msg__Target));
  bool success = avai_messages__msg__Target__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
avai_messages__msg__Target__destroy(avai_messages__msg__Target * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    avai_messages__msg__Target__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
avai_messages__msg__Target__Sequence__init(avai_messages__msg__Target__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Target * data = NULL;

  if (size) {
    data = (avai_messages__msg__Target *)allocator.zero_allocate(size, sizeof(avai_messages__msg__Target), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = avai_messages__msg__Target__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        avai_messages__msg__Target__fini(&data[i - 1]);
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
avai_messages__msg__Target__Sequence__fini(avai_messages__msg__Target__Sequence * array)
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
      avai_messages__msg__Target__fini(&array->data[i]);
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

avai_messages__msg__Target__Sequence *
avai_messages__msg__Target__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  avai_messages__msg__Target__Sequence * array = (avai_messages__msg__Target__Sequence *)allocator.allocate(sizeof(avai_messages__msg__Target__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = avai_messages__msg__Target__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
avai_messages__msg__Target__Sequence__destroy(avai_messages__msg__Target__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    avai_messages__msg__Target__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
avai_messages__msg__Target__Sequence__are_equal(const avai_messages__msg__Target__Sequence * lhs, const avai_messages__msg__Target__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!avai_messages__msg__Target__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
avai_messages__msg__Target__Sequence__copy(
  const avai_messages__msg__Target__Sequence * input,
  avai_messages__msg__Target__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(avai_messages__msg__Target);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    avai_messages__msg__Target * data =
      (avai_messages__msg__Target *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!avai_messages__msg__Target__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          avai_messages__msg__Target__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!avai_messages__msg__Target__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
