// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/YoloOutput.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__YOLO_OUTPUT__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__YOLO_OUTPUT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/yolo_output__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_YoloOutput_bounding_boxes
{
public:
  explicit Init_YoloOutput_bounding_boxes(::avai_messages::msg::YoloOutput & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::YoloOutput bounding_boxes(::avai_messages::msg::YoloOutput::_bounding_boxes_type arg)
  {
    msg_.bounding_boxes = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::YoloOutput msg_;
};

class Init_YoloOutput_header
{
public:
  Init_YoloOutput_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_YoloOutput_bounding_boxes header(::avai_messages::msg::YoloOutput::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_YoloOutput_bounding_boxes(msg_);
  }

private:
  ::avai_messages::msg::YoloOutput msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::YoloOutput>()
{
  return avai_messages::msg::builder::Init_YoloOutput_header();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__YOLO_OUTPUT__BUILDER_HPP_
