// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from avai_messages:msg/VehicleLights.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__TRAITS_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "avai_messages/msg/detail/vehicle_lights__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace avai_messages
{

namespace msg
{

inline void to_flow_style_yaml(
  const VehicleLights & msg,
  std::ostream & out)
{
  out << "{";
  // member: left_motor
  {
    out << "left_motor: ";
    rosidl_generator_traits::value_to_yaml(msg.left_motor, out);
    out << ", ";
  }

  // member: right_motor
  {
    out << "right_motor: ";
    rosidl_generator_traits::value_to_yaml(msg.right_motor, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const VehicleLights & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: left_motor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "left_motor: ";
    rosidl_generator_traits::value_to_yaml(msg.left_motor, out);
    out << "\n";
  }

  // member: right_motor
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "right_motor: ";
    rosidl_generator_traits::value_to_yaml(msg.right_motor, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const VehicleLights & msg, bool use_flow_style = false)
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
  const avai_messages::msg::VehicleLights & msg,
  std::ostream & out, size_t indentation = 0)
{
  avai_messages::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use avai_messages::msg::to_yaml() instead")]]
inline std::string to_yaml(const avai_messages::msg::VehicleLights & msg)
{
  return avai_messages::msg::to_yaml(msg);
}

template<>
inline const char * data_type<avai_messages::msg::VehicleLights>()
{
  return "avai_messages::msg::VehicleLights";
}

template<>
inline const char * name<avai_messages::msg::VehicleLights>()
{
  return "avai_messages/msg/VehicleLights";
}

template<>
struct has_fixed_size<avai_messages::msg::VehicleLights>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<avai_messages::msg::VehicleLights>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<avai_messages::msg::VehicleLights>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__TRAITS_HPP_
