// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from avai_messages:msg/Cones.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "avai_messages/msg/detail/cones__struct.hpp"
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

void Cones_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) avai_messages::msg::Cones(_init);
}

void Cones_fini_function(void * message_memory)
{
  auto typed_message = static_cast<avai_messages::msg::Cones *>(message_memory);
  typed_message->~Cones();
}

size_t size_function__Cones__cones(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<avai_messages::msg::Cone> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Cones__cones(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<avai_messages::msg::Cone> *>(untyped_member);
  return &member[index];
}

void * get_function__Cones__cones(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<avai_messages::msg::Cone> *>(untyped_member);
  return &member[index];
}

void fetch_function__Cones__cones(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const avai_messages::msg::Cone *>(
    get_const_function__Cones__cones(untyped_member, index));
  auto & value = *reinterpret_cast<avai_messages::msg::Cone *>(untyped_value);
  value = item;
}

void assign_function__Cones__cones(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<avai_messages::msg::Cone *>(
    get_function__Cones__cones(untyped_member, index));
  const auto & value = *reinterpret_cast<const avai_messages::msg::Cone *>(untyped_value);
  item = value;
}

void resize_function__Cones__cones(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<avai_messages::msg::Cone> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Cones_message_member_array[2] = {
  {
    "header",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<std_msgs::msg::Header>(),  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages::msg::Cones, header),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "cones",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<avai_messages::msg::Cone>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(avai_messages::msg::Cones, cones),  // bytes offset in struct
    nullptr,  // default value
    size_function__Cones__cones,  // size() function pointer
    get_const_function__Cones__cones,  // get_const(index) function pointer
    get_function__Cones__cones,  // get(index) function pointer
    fetch_function__Cones__cones,  // fetch(index, &value) function pointer
    assign_function__Cones__cones,  // assign(index, value) function pointer
    resize_function__Cones__cones  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Cones_message_members = {
  "avai_messages::msg",  // message namespace
  "Cones",  // message name
  2,  // number of fields
  sizeof(avai_messages::msg::Cones),
  Cones_message_member_array,  // message members
  Cones_init_function,  // function to initialize message memory (memory has to be allocated)
  Cones_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Cones_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Cones_message_members,
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
get_message_type_support_handle<avai_messages::msg::Cones>()
{
  return &::avai_messages::msg::rosidl_typesupport_introspection_cpp::Cones_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, avai_messages, msg, Cones)() {
  return &::avai_messages::msg::rosidl_typesupport_introspection_cpp::Cones_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
