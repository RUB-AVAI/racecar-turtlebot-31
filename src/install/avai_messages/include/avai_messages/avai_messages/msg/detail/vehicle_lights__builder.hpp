// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/VehicleLights.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/vehicle_lights__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_VehicleLights_right_motor
{
public:
  explicit Init_VehicleLights_right_motor(::avai_messages::msg::VehicleLights & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::VehicleLights right_motor(::avai_messages::msg::VehicleLights::_right_motor_type arg)
  {
    msg_.right_motor = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::VehicleLights msg_;
};

class Init_VehicleLights_left_motor
{
public:
  Init_VehicleLights_left_motor()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_VehicleLights_right_motor left_motor(::avai_messages::msg::VehicleLights::_left_motor_type arg)
  {
    msg_.left_motor = std::move(arg);
    return Init_VehicleLights_right_motor(msg_);
  }

private:
  ::avai_messages::msg::VehicleLights msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::VehicleLights>()
{
  return avai_messages::msg::builder::Init_VehicleLights_left_motor();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__BUILDER_HPP_
