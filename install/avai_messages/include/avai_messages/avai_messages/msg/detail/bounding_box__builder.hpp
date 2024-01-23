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

class Init_BoundingBox_cone
{
public:
  explicit Init_BoundingBox_cone(::avai_messages::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::BoundingBox cone(::avai_messages::msg::BoundingBox::_cone_type arg)
  {
    msg_.cone = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::BoundingBox msg_;
};

class Init_BoundingBox_confidence
{
public:
  explicit Init_BoundingBox_confidence(::avai_messages::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  Init_BoundingBox_cone confidence(::avai_messages::msg::BoundingBox::_confidence_type arg)
  {
    msg_.confidence = std::move(arg);
    return Init_BoundingBox_cone(msg_);
  }

private:
  ::avai_messages::msg::BoundingBox msg_;
};

class Init_BoundingBox_max_y
{
public:
  explicit Init_BoundingBox_max_y(::avai_messages::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  Init_BoundingBox_confidence max_y(::avai_messages::msg::BoundingBox::_max_y_type arg)
  {
    msg_.max_y = std::move(arg);
    return Init_BoundingBox_confidence(msg_);
  }

private:
  ::avai_messages::msg::BoundingBox msg_;
};

class Init_BoundingBox_max_x
{
public:
  explicit Init_BoundingBox_max_x(::avai_messages::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  Init_BoundingBox_max_y max_x(::avai_messages::msg::BoundingBox::_max_x_type arg)
  {
    msg_.max_x = std::move(arg);
    return Init_BoundingBox_max_y(msg_);
  }

private:
  ::avai_messages::msg::BoundingBox msg_;
};

class Init_BoundingBox_min_y
{
public:
  explicit Init_BoundingBox_min_y(::avai_messages::msg::BoundingBox & msg)
  : msg_(msg)
  {}
  Init_BoundingBox_max_x min_y(::avai_messages::msg::BoundingBox::_min_y_type arg)
  {
    msg_.min_y = std::move(arg);
    return Init_BoundingBox_max_x(msg_);
  }

private:
  ::avai_messages::msg::BoundingBox msg_;
};

class Init_BoundingBox_min_x
{
public:
  Init_BoundingBox_min_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_BoundingBox_min_y min_x(::avai_messages::msg::BoundingBox::_min_x_type arg)
  {
    msg_.min_x = std::move(arg);
    return Init_BoundingBox_min_y(msg_);
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
  return avai_messages::msg::builder::Init_BoundingBox_min_x();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__BUILDER_HPP_
