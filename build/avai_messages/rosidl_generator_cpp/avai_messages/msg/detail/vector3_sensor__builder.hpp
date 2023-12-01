// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avai_messages:msg/Vector3Sensor.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__VECTOR3_SENSOR__BUILDER_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__VECTOR3_SENSOR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "avai_messages/msg/detail/vector3_sensor__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace avai_messages
{

namespace msg
{

namespace builder
{

class Init_Vector3Sensor_update_time
{
public:
  explicit Init_Vector3Sensor_update_time(::avai_messages::msg::Vector3Sensor & msg)
  : msg_(msg)
  {}
  ::avai_messages::msg::Vector3Sensor update_time(::avai_messages::msg::Vector3Sensor::_update_time_type arg)
  {
    msg_.update_time = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avai_messages::msg::Vector3Sensor msg_;
};

class Init_Vector3Sensor_data
{
public:
  explicit Init_Vector3Sensor_data(::avai_messages::msg::Vector3Sensor & msg)
  : msg_(msg)
  {}
  Init_Vector3Sensor_update_time data(::avai_messages::msg::Vector3Sensor::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_Vector3Sensor_update_time(msg_);
  }

private:
  ::avai_messages::msg::Vector3Sensor msg_;
};

class Init_Vector3Sensor_header
{
public:
  Init_Vector3Sensor_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Vector3Sensor_data header(::avai_messages::msg::Vector3Sensor::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_Vector3Sensor_data(msg_);
  }

private:
  ::avai_messages::msg::Vector3Sensor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avai_messages::msg::Vector3Sensor>()
{
  return avai_messages::msg::builder::Init_Vector3Sensor_header();
}

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__VECTOR3_SENSOR__BUILDER_HPP_
