// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from avai_messages:msg/Motors.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "avai_messages/msg/detail/motors__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace avai_messages
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Motors_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) avai_messages::msg::Motors(_init);
}

void Motors_fini_function(void * message_memory)
{
  auto typed_message = static_cast<avai_messages::msg::Motors *>(message_memory);
  typed_message->~Motors();
}

size_t size_function__Motors__motors(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<avai_messages::msg::Motor> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Motors__motors(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<avai_messages::msg::Motor> *>(untyped_member);
  return &member[index];
}

void * get_function__Motors__motors(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<avai_messages::msg::Motor> *>(untyped_member);
  return &member[index];
}

void fetch_function__Motors__motors(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const avai_messages::msg::Motor *>(
    get_const_function__Motors__motors(untyped_member, index));
  auto & value = *reinterpret_cast<avai_messages::msg::Motor *>(untyped_value);
  value = item;
}

void assign_function__Motors__motors(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<avai_messages::msg::Motor *>(
    get_function__Motors__motors(untyped_member, index));
  const auto & value = *reinterpret_cast<const avai_messages::msg::Motor *>(untyped_value);
  item = value;
}

void resize_function__Motors__motors(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<avai_messages::msg::Motor> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Motors_message_member_array[1] = {
  {
    "motors",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<avai_messages::msg::Motor>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages::msg::Motors, motors),  // bytes offset in struct
    nullptr,  // default value
    size_function__Motors__motors,  // size() function pointer
    get_const_function__Motors__motors,  // get_const(index) function pointer
    get_function__Motors__motors,  // get(index) function pointer
    fetch_function__Motors__motors,  // fetch(index, &value) function pointer
    assign_function__Motors__motors,  // assign(index, value) function pointer
    resize_function__Motors__motors  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Motors_message_members = {
  "avai_messages::msg",  // message namespace
  "Motors",  // message name
  1,  // number of fields
  sizeof(avai_messages::msg::Motors),
  Motors_message_member_array,  // message members
  Motors_init_function,  // function to initialize message memory (memory has to be allocated)
  Motors_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Motors_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Motors_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace avai_messages


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<avai_messages::msg::Motors>()
{
  return &::avai_messages::msg::rosidl_typesupport_introspection_cpp::Motors_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, avai_messages, msg, Motors)() {
  return &::avai_messages::msg::rosidl_typesupport_introspection_cpp::Motors_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
