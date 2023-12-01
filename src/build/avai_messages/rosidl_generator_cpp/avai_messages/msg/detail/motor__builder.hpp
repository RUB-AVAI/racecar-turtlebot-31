// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/Motor.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__MOTOR__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__MOTOR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/motor__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_Motor_velocity
{
public:
  explicit Init_Motor_velocity(::avai_messages::msg::Motor & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::Motor velocity(::avai_messages::msg::Motor::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::Motor msg_;
};

class Init_Motor_position
{
public:
  Init_Motor_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Motor_velocity position(::avai_messages::msg::Motor::_position_type arg)
  {
    msg_.position = std::move(arg);
    return Init_Motor_velocity(msg_);
  }

private:
  ::avai_messages::msg::Motor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::Motor>()
{
  return avai_messages::msg::builder::Init_Motor_position();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__MOTOR__BUILDER_HPP_
