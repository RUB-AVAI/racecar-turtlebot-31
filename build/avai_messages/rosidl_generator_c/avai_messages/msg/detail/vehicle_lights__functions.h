// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from avai_messages:msg/VehicleLights.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__FUNCTIONS_H_
#define AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "avai_messages/msg/rosidl_generator_c__visibility_control.h"

#include "avai_messages/msg/detail/vehicle_lights__struct.h"

/// Initialize msg/VehicleLights message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * avai_messages__msg__VehicleLights
 * )) before or use
 * avai_messages__msg__VehicleLights__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
bool
avai_messages__msg__VehicleLights__init(avai_messages__msg__VehicleLights * msg);

/// Finalize msg/VehicleLights message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
void
avai_messages__msg__VehicleLights__fini(avai_messages__msg__VehicleLights * msg);

/// Create msg/VehicleLights message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * avai_messages__msg__VehicleLights__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
avai_messages__msg__VehicleLights *
avai_messages__msg__VehicleLights__create();

/// Destroy msg/VehicleLights message.
/**
 * It calls
 * avai_messages__msg__VehicleLights__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
void
avai_messages__msg__VehicleLights__destroy(avai_messages__msg__VehicleLights * msg);

/// Check for msg/VehicleLights message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
bool
avai_messages__msg__VehicleLights__are_equal(const avai_messages__msg__VehicleLights * lhs, const avai_messages__msg__VehicleLights * rhs);

/// Copy a msg/VehicleLights message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
bool
avai_messages__msg__VehicleLights__copy(
  const avai_messages__msg__VehicleLights * input,
  avai_messages__msg__VehicleLights * output);

/// Initialize array of msg/VehicleLights messages.
/**
 * It allocates the memory for the number of elements and calls
 * avai_messages__msg__VehicleLights__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
bool
avai_messages__msg__VehicleLights__Sequence__init(avai_messages__msg__VehicleLights__Sequence * array, size_t size);

/// Finalize array of msg/VehicleLights messages.
/**
 * It calls
 * avai_messages__msg__VehicleLights__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
void
avai_messages__msg__VehicleLights__Sequence__fini(avai_messages__msg__VehicleLights__Sequence * array);

/// Create array of msg/VehicleLights messages.
/**
 * It allocates the memory for the array and calls
 * avai_messages__msg__VehicleLights__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
avai_messages__msg__VehicleLights__Sequence *
avai_messages__msg__VehicleLights__Sequence__create(size_t size);

/// Destroy array of msg/VehicleLights messages.
/**
 * It calls
 * avai_messages__msg__VehicleLights__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
void
avai_messages__msg__VehicleLights__Sequence__destroy(avai_messages__msg__VehicleLights__Sequence * array);

/// Check for msg/VehicleLights message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
bool
avai_messages__msg__VehicleLights__Sequence__are_equal(const avai_messages__msg__VehicleLights__Sequence * lhs, const avai_messages__msg__VehicleLights__Sequence * rhs);

/// Copy an array of msg/VehicleLights messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_avai_messages
bool
avai_messages__msg__VehicleLights__Sequence__copy(
  const avai_messages__msg__VehicleLights__Sequence * input,
  avai_messages__msg__VehicleLights__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__FUNCTIONS_H_
