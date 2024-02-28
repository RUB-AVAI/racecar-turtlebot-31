// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/ClusteredLidarData.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__CLUSTERED_LIDAR_DATA__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__CLUSTERED_LIDAR_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/clustered_lidar_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_ClusteredLidarData_clusters
{
public:
  explicit Init_ClusteredLidarData_clusters(::avai_messages::msg::ClusteredLidarData & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::ClusteredLidarData clusters(::avai_messages::msg::ClusteredLidarData::_clusters_type arg)
  {
    msg_.clusters = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::ClusteredLidarData msg_;
};

class Init_ClusteredLidarData_header
{
public:
  Init_ClusteredLidarData_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ClusteredLidarData_clusters header(::avai_messages::msg::ClusteredLidarData::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_ClusteredLidarData_clusters(msg_);
  }

private:
  ::avai_messages::msg::ClusteredLidarData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::ClusteredLidarData>()
{
  return avai_messages::msg::builder::Init_ClusteredLidarData_header();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__CLUSTERED_LIDAR_DATA__BUILDER_HPP_
