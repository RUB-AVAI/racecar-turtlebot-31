// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/Cluster.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__CLUSTER__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__CLUSTER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/cluster__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_Cluster_ranges
{
public:
  explicit Init_Cluster_ranges(::avai_messages::msg::Cluster & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::Cluster ranges(::avai_messages::msg::Cluster::_ranges_type arg)
  {
    msg_.ranges = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::Cluster msg_;
};

class Init_Cluster_angles
{
public:
  explicit Init_Cluster_angles(::avai_messages::msg::Cluster & msg)
  : msg_(msg)
  {}
  Init_Cluster_ranges angles(::avai_messages::msg::Cluster::_angles_type arg)
  {
    msg_.angles = std::move(arg);
    return Init_Cluster_ranges(msg_);
  }

private:
  ::avai_messages::msg::Cluster msg_;
};

class Init_Cluster_y_positions
{
public:
  explicit Init_Cluster_y_positions(::avai_messages::msg::Cluster & msg)
  : msg_(msg)
  {}
  Init_Cluster_angles y_positions(::avai_messages::msg::Cluster::_y_positions_type arg)
  {
    msg_.y_positions = std::move(arg);
    return Init_Cluster_angles(msg_);
  }

private:
  ::avai_messages::msg::Cluster msg_;
};

class Init_Cluster_x_positions
{
public:
  Init_Cluster_x_positions()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Cluster_y_positions x_positions(::avai_messages::msg::Cluster::_x_positions_type arg)
  {
    msg_.x_positions = std::move(arg);
    return Init_Cluster_y_positions(msg_);
  }

private:
  ::avai_messages::msg::Cluster msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::Cluster>()
{
  return avai_messages::msg::builder::Init_Cluster_x_positions();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__CLUSTER__BUILDER_HPP_
