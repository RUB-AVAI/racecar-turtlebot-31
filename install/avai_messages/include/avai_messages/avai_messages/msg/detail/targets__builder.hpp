// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/Targets.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__TARGETS__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__TARGETS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/targets__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_Targets_round
{
public:
  explicit Init_Targets_round(::avai_messages::msg::Targets & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::Targets round(::avai_messages::msg::Targets::_round_type arg)
  {
    msg_.round = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::Targets msg_;
};

class Init_Targets_y_position
{
public:
  explicit Init_Targets_y_position(::avai_messages::msg::Targets & msg)
  : msg_(msg)
  {}
  Init_Targets_round y_position(::avai_messages::msg::Targets::_y_position_type arg)
  {
    msg_.y_position = std::move(arg);
    return Init_Targets_round(msg_);
  }

private:
  ::avai_messages::msg::Targets msg_;
};

class Init_Targets_x_position
{
public:
  Init_Targets_x_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Targets_y_position x_position(::avai_messages::msg::Targets::_x_position_type arg)
  {
    msg_.x_position = std::move(arg);
    return Init_Targets_y_position(msg_);
  }

private:
  ::avai_messages::msg::Targets msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::Targets>()
{
  return avai_messages::msg::builder::Init_Targets_x_position();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__TARGETS__BUILDER_HPP_
