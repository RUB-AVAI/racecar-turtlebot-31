// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/Target.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__TARGET__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__TARGET__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/target__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_Target_turn_angle
{
public:
  explicit Init_Target_turn_angle(::avai_messages::msg::Target & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::Target turn_angle(::avai_messages::msg::Target::_turn_angle_type arg)
  {
    msg_.turn_angle = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::Target msg_;
};

class Init_Target_round
{
public:
  explicit Init_Target_round(::avai_messages::msg::Target & msg)
  : msg_(msg)
  {}
  Init_Target_turn_angle round(::avai_messages::msg::Target::_round_type arg)
  {
    msg_.round = std::move(arg);
    return Init_Target_turn_angle(msg_);
  }

private:
  ::avai_messages::msg::Target msg_;
};

class Init_Target_y_position
{
public:
  explicit Init_Target_y_position(::avai_messages::msg::Target & msg)
  : msg_(msg)
  {}
  Init_Target_round y_position(::avai_messages::msg::Target::_y_position_type arg)
  {
    msg_.y_position = std::move(arg);
    return Init_Target_round(msg_);
  }

private:
  ::avai_messages::msg::Target msg_;
};

class Init_Target_x_position
{
public:
  explicit Init_Target_x_position(::avai_messages::msg::Target & msg)
  : msg_(msg)
  {}
  Init_Target_y_position x_position(::avai_messages::msg::Target::_x_position_type arg)
  {
    msg_.x_position = std::move(arg);
    return Init_Target_y_position(msg_);
  }

private:
  ::avai_messages::msg::Target msg_;
};

class Init_Target_header
{
public:
  Init_Target_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Target_x_position header(::avai_messages::msg::Target::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Target_x_position(msg_);
  }

private:
  ::avai_messages::msg::Target msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::Target>()
{
  return avai_messages::msg::builder::Init_Target_header();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__TARGET__BUILDER_HPP_
