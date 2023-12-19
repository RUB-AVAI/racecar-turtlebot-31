// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/bounding_box__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_BoundingBox_label
{
public:
  explicit Init_BoundingBox_label(::avai_messages::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::BoundingBox label(::avai_messages::msg::BoundingBox::_label_type arg)
  {
    msg_.label = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::BoundingBox msg_;
};

class Init_BoundingBox_height
{
public:
  explicit Init_BoundingBox_height(::avai_messages::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  Init_BoundingBox_label height(::avai_messages::msg::BoundingBox::_height_type arg)
  {
    msg_.height = std::move(arg);
    return Init_BoundingBox_label(msg_);
  }

private:
  ::avai_messages::msg::BoundingBox msg_;
};

class Init_BoundingBox_width
{
public:
  explicit Init_BoundingBox_width(::avai_messages::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  Init_BoundingBox_height width(::avai_messages::msg::BoundingBox::_width_type arg)
  {
    msg_.width = std::move(arg);
    return Init_BoundingBox_height(msg_);
  }

private:
  ::avai_messages::msg::BoundingBox msg_;
};

class Init_BoundingBox_y
{
public:
  explicit Init_BoundingBox_y(::avai_messages::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  Init_BoundingBox_width y(::avai_messages::msg::BoundingBox::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_BoundingBox_width(msg_);
  }

private:
  ::avai_messages::msg::BoundingBox msg_;
};

class Init_BoundingBox_x
{
public:
  Init_BoundingBox_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BoundingBox_y x(::avai_messages::msg::BoundingBox::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_BoundingBox_y(msg_);
  }

private:
  ::avai_messages::msg::BoundingBox msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::BoundingBox>()
{
  return avai_messages::msg::builder::Init_BoundingBox_x();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__BUILDER_HPP_
