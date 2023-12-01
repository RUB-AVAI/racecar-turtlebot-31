// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avai_messages:msg/Vector3Sensor.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__VECTOR3_SENSOR__STRUCT_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__VECTOR3_SENSOR__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"
// Member 'data'
#include "geometry_msgs/msg/detail/vector3__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__avai_messages__msg__Vector3Sensor __attribute__((deprecated))
#else
# define DEPRECATED__avai_messages__msg__Vector3Sensor __declspec(deprecated)
#endif

namespace avai_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Vector3Sensor_
{
  using Type = Vector3Sensor_<ContainerAllocator>;

  explicit Vector3Sensor_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init),
    data(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->update_time = 0l;
    }
  }

  explicit Vector3Sensor_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init),
    data(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->update_time = 0l;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _data_type =
    geometry_msgs::msg::Vector3_<ContainerAllocator>;
  _data_type data;
  using _update_time_type =
    int32_t;
  _update_time_type update_time;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__data(
    const geometry_msgs::msg::Vector3_<ContainerAllocator> & _arg)
  {
    this->data = _arg;
    return *this;
  }
  Type & set__update_time(
    const int32_t & _arg)
  {
    this->update_time = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avai_messages::msg::Vector3Sensor_<ContainerAllocator> *;
  using ConstRawPtr =
    const avai_messages::msg::Vector3Sensor_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avai_messages::msg::Vector3Sensor_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avai_messages::msg::Vector3Sensor_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::Vector3Sensor_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::Vector3Sensor_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::Vector3Sensor_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::Vector3Sensor_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avai_messages::msg::Vector3Sensor_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avai_messages::msg::Vector3Sensor_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avai_messages__msg__Vector3Sensor
    std::shared_ptr<avai_messages::msg::Vector3Sensor_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avai_messages__msg__Vector3Sensor
    std::shared_ptr<avai_messages::msg::Vector3Sensor_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Vector3Sensor_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    if (this->update_time != other.update_time) {
      return false;
    }
    return true;
  }
  bool operator!=(const Vector3Sensor_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Vector3Sensor_

// alias to use template instance with default allocator
using Vector3Sensor =
  avai_messages::msg::Vector3Sensor_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__VECTOR3_SENSOR__STRUCT_HPP_
