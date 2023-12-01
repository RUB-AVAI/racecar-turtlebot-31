// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/Melody.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__MELODY__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__MELODY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/melody__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_Melody_duration
{
public:
  explicit Init_Melody_duration(::avai_messages::msg::Melody & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::Melody duration(::avai_messages::msg::Melody::_duration_type arg)
  {
    msg_.duration = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::Melody msg_;
};

class Init_Melody_pitch
{
public:
  explicit Init_Melody_pitch(::avai_messages::msg::Melody & msg)
  : msg_(msg)
  {}
  Init_Melody_duration pitch(::avai_messages::msg::Melody::_pitch_type arg)
  {
    msg_.pitch = std::move(arg);
    return Init_Melody_duration(msg_);
  }

private:
  ::avai_messages::msg::Melody msg_;
};

class Init_Melody_length
{
public:
  Init_Melody_length()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Melody_pitch length(::avai_messages::msg::Melody::_length_type arg)
  {
    msg_.length = std::move(arg);
    return Init_Melody_pitch(msg_);
  }

private:
  ::avai_messages::msg::Melody msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::Melody>()
{
  return avai_messages::msg::builder::Init_Melody_length();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__MELODY__BUILDER_HPP_
