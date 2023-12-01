// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avai_messages:msg/VehicleLights.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__STRUCT_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__avai_messages__msg__VehicleLights __attribute__((deprecated))
#else
# define DEPRECATED__avai_messages__msg__VehicleLights __declspec(deprecated)
#endif

namespace avai_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct VehicleLights_
{
  using Type = VehicleLights_<ContainerAllocator>;

  explicit VehicleLights_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_motor = false;
      this->right_motor = false;
    }
  }

  explicit VehicleLights_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->left_motor = false;
      this->right_motor = false;
    }
  }

  // field types and members
  using _left_motor_type =
    bool;
  _left_motor_type left_motor;
  using _right_motor_type =
    bool;
  _right_motor_type right_motor;

  // setters for named parameter idiom
  Type & set__left_motor(
    const bool & _arg)
  {
    this->left_motor = _arg;
    return *this;
  }
  Type & set__right_motor(
    const bool & _arg)
  {
    this->right_motor = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avai_messages::msg::VehicleLights_<ContainerAllocator> *;
  using ConstRawPtr =
    const avai_messages::msg::VehicleLights_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avai_messages::msg::VehicleLights_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avai_messages::msg::VehicleLights_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::VehicleLights_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::VehicleLights_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::VehicleLights_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::VehicleLights_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avai_messages::msg::VehicleLights_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avai_messages::msg::VehicleLights_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avai_messages__msg__VehicleLights
    std::shared_ptr<avai_messages::msg::VehicleLights_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avai_messages__msg__VehicleLights
    std::shared_ptr<avai_messages::msg::VehicleLights_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const VehicleLights_ & other) const
  {
    if (this->left_motor != other.left_motor) {
      return false;
    }
    if (this->right_motor != other.right_motor) {
      return false;
    }
    return true;
  }
  bool operator!=(const VehicleLights_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct VehicleLights_

// alias to use template instance with default allocator
using VehicleLights =
  avai_messages::msg::VehicleLights_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__VEHICLE_LIGHTS__STRUCT_HPP_
