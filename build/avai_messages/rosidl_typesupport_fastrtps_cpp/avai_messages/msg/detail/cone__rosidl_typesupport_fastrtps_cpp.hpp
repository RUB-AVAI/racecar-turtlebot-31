// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from avai_messages:msg/Cone.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__CONE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__CONE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "avai_messages/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "avai_messages/msg/detail/cone__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace avai_messages
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avai_messages
cdr_serialize(
  const avai_messages::msg::Cone & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avai_messages
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  avai_messages::msg::Cone & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avai_messages
get_serialized_size(
  const avai_messages::msg::Cone & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avai_messages
max_serialized_size_Cone(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace avai_messages

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_avai_messages
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, avai_messages, msg, Cone)();

#ifdef __cplusplus
}
#endif

#endif  // AVAI_MESSAGES__MSG__DETAIL__CONE__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
