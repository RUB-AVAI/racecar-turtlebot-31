// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from avai_messages:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__TRAITS_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "avai_messages/msg/detail/bounding_box__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace avai_messages
{

namespace msg
{

inline void to_flow_style_yaml(
  const BoundingBox & msg,
  std::ostream & out)
{
  out << "{";
  // member: min_x
  {
    out << "min_x: ";
    rosidl_generator_traits::value_to_yaml(msg.min_x, out);
    out << ", ";
  }

  // member: min_y
  {
    out << "min_y: ";
    rosidl_generator_traits::value_to_yaml(msg.min_y, out);
    out << ", ";
  }

  // member: max_x
  {
    out << "max_x: ";
    rosidl_generator_traits::value_to_yaml(msg.max_x, out);
    out << ", ";
  }

  // member: max_y
  {
    out << "max_y: ";
    rosidl_generator_traits::value_to_yaml(msg.max_y, out);
    out << ", ";
  }

  // member: confidence
  {
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << ", ";
  }

  // member: cone
  {
    out << "cone: ";
    rosidl_generator_traits::value_to_yaml(msg.cone, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const BoundingBox & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: min_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "min_x: ";
    rosidl_generator_traits::value_to_yaml(msg.min_x, out);
    out << "\n";
  }

  // member: min_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "min_y: ";
    rosidl_generator_traits::value_to_yaml(msg.min_y, out);
    out << "\n";
  }

  // member: max_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "max_x: ";
    rosidl_generator_traits::value_to_yaml(msg.max_x, out);
    out << "\n";
  }

  // member: max_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "max_y: ";
    rosidl_generator_traits::value_to_yaml(msg.max_y, out);
    out << "\n";
  }

  // member: confidence
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "confidence: ";
    rosidl_generator_traits::value_to_yaml(msg.confidence, out);
    out << "\n";
  }

  // member: cone
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cone: ";
    rosidl_generator_traits::value_to_yaml(msg.cone, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const BoundingBox & msg, bool use_flow_style = false)
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
  const avai_messages::msg::BoundingBox & msg,
  std::ostream & out, size_t indentation = 0)
{
  avai_messages::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use avai_messages::msg::to_yaml() instead")]]
inline std::string to_yaml(const avai_messages::msg::BoundingBox & msg)
{
  return avai_messages::msg::to_yaml(msg);
}

template<>
inline const char * data_type<avai_messages::msg::BoundingBox>()
{
  return "avai_messages::msg::BoundingBox";
}

template<>
inline const char * name<avai_messages::msg::BoundingBox>()
{
  return "avai_messages/msg/BoundingBox";
}

template<>
struct has_fixed_size<avai_messages::msg::BoundingBox>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<avai_messages::msg::BoundingBox>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<avai_messages::msg::BoundingBox>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__TRAITS_HPP_
