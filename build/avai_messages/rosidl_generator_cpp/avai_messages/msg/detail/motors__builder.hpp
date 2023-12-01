// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/Motors.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__MOTORS__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__MOTORS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/motors__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_Motors_motors
{
public:
  Init_Motors_motors()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::avai_messages::msg::Motors motors(::avai_messages::msg::Motors::_motors_type arg)
  {
    msg_.motors = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::Motors msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::Motors>()
{
  return avai_messages::msg::builder::Init_Motors_motors();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__MOTORS__BUILDER_HPP_
