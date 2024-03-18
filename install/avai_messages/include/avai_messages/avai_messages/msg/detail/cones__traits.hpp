// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from avai_messages:msg/Cones.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__CONES__TRAITS_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__CONES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "avai_messages/msg/detail/cones__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'cones'
#include "avai_messages/msg/detail/cone__traits.hpp"

namespace avai_messages
{

namespace msg
{

inline void to_flow_style_yaml(
  const Cones & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: cones
  {
    if (msg.cones.size() == 0) {
      out << "cones: []";
    } else {
      out << "cones: [";
      size_t pending_items = msg.cones.size();
      for (auto item : msg.cones) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Cones & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: cones
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.cones.size() == 0) {
      out << "cones: []\n";
    } else {
      out << "cones:\n";
      for (auto item : msg.cones) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Cones & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace avai_messages

namespace rosidl_generator_traits
{

[[deprecated("use avai_messages::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const avai_messages::msg::Cones & msg,
  std::ostream & out, size_t indentation = 0)
{
  avai_messages::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use avai_messages::msg::to_yaml() instead")]]
inline std::string to_yaml(const avai_messages::msg::Cones & msg)
{
  return avai_messages::msg::to_yaml(msg);
}

template<>
inline const char * data_type<avai_messages::msg::Cones>()
{
  return "avai_messages::msg::Cones";
}

template<>
inline const char * name<avai_messages::msg::Cones>()
{
  return "avai_messages/msg/Cones";
}

template<>
struct has_fixed_size<avai_messages::msg::Cones>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<avai_messages::msg::Cones>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<avai_messages::msg::Cones>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AVAI_MESSAGES__MSG__DETAIL__CONES__TRAITS_HPP_
