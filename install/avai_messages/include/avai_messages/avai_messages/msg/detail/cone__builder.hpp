// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/Cone.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__CONE__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__CONE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/cone__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_Cone_y_position
{
public:
  explicit Init_Cone_y_position(::avai_messages::msg::Cone & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::Cone y_position(::avai_messages::msg::Cone::_y_position_type arg)
  {
    msg_.y_position = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::Cone msg_;
};

class Init_Cone_x_position
{
public:
  explicit Init_Cone_x_position(::avai_messages::msg::Cone & msg)
  : msg_(msg)
  {}
  Init_Cone_y_position x_position(::avai_messages::msg::Cone::_x_position_type arg)
  {
    msg_.x_position = std::move(arg);
    return Init_Cone_y_position(msg_);
  }

private:
  ::avai_messages::msg::Cone msg_;
};

class Init_Cone_color
{
public:
  Init_Cone_color()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Cone_x_position color(::avai_messages::msg::Cone::_color_type arg)
  {
    msg_.color = std::move(arg);
    return Init_Cone_x_position(msg_);
  }

private:
  ::avai_messages::msg::Cone msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::Cone>()
{
  return avai_messages::msg::builder::Init_Cone_color();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__CONE__BUILDER_HPP_
