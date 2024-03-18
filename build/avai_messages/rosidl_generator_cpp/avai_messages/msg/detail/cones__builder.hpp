// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/Cones.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__CONES__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__CONES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/cones__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_Cones_cones
{
public:
  explicit Init_Cones_cones(::avai_messages::msg::Cones & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::Cones cones(::avai_messages::msg::Cones::_cones_type arg)
  {
    msg_.cones = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::Cones msg_;
};

class Init_Cones_header
{
public:
  Init_Cones_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Cones_cones header(::avai_messages::msg::Cones::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Cones_cones(msg_);
  }

private:
  ::avai_messages::msg::Cones msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::Cones>()
{
  return avai_messages::msg::builder::Init_Cones_header();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__CONES__BUILDER_HPP_
