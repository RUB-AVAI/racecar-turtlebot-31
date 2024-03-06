// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/Position.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__POSITION__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__POSITION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/position__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_Position_facing_direction
{
public:
  explicit Init_Position_facing_direction(::avai_messages::msg::Position & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::Position facing_direction(::avai_messages::msg::Position::_facing_direction_type arg)
  {
    msg_.facing_direction = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::Position msg_;
};

class Init_Position_y_position
{
public:
  explicit Init_Position_y_position(::avai_messages::msg::Position & msg)
  : msg_(msg)
  {}
  Init_Position_facing_direction y_position(::avai_messages::msg::Position::_y_position_type arg)
  {
    msg_.y_position = std::move(arg);
    return Init_Position_facing_direction(msg_);
  }

private:
  ::avai_messages::msg::Position msg_;
};

class Init_Position_x_position
{
public:
  explicit Init_Position_x_position(::avai_messages::msg::Position & msg)
  : msg_(msg)
  {}
  Init_Position_y_position x_position(::avai_messages::msg::Position::_x_position_type arg)
  {
    msg_.x_position = std::move(arg);
    return Init_Position_y_position(msg_);
  }

private:
  ::avai_messages::msg::Position msg_;
};

class Init_Position_header
{
public:
  Init_Position_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Position_x_position header(::avai_messages::msg::Position::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Position_x_position(msg_);
  }

private:
  ::avai_messages::msg::Position msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::Position>()
{
  return avai_messages::msg::builder::Init_Position_header();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__POSITION__BUILDER_HPP_
