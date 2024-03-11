// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avai_messages:msg/Targets.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__TARGETS__STRUCT_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__TARGETS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__avai_messages__msg__Targets __attribute__((deprecated))
#else
# define DEPRECATED__avai_messages__msg__Targets __declspec(deprecated)
#endif

namespace avai_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Targets_
{
  using Type = Targets_<ContainerAllocator>;

  explicit Targets_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x_position = 0.0;
      this->y_position = 0.0;
      this->round = 0;
    }
  }

  explicit Targets_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x_position = 0.0;
      this->y_position = 0.0;
      this->round = 0;
    }
  }

  // field types and members
  using _x_position_type =
    double;
  _x_position_type x_position;
  using _y_position_type =
    double;
  _y_position_type y_position;
  using _round_type =
    int8_t;
  _round_type round;

  // setters for named parameter idiom
  Type & set__x_position(
    const double & _arg)
  {
    this->x_position = _arg;
    return *this;
  }
  Type & set__y_position(
    const double & _arg)
  {
    this->y_position = _arg;
    return *this;
  }
  Type & set__round(
    const int8_t & _arg)
  {
    this->round = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avai_messages::msg::Targets_<ContainerAllocator> *;
  using ConstRawPtr =
    const avai_messages::msg::Targets_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avai_messages::msg::Targets_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avai_messages::msg::Targets_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::Targets_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::Targets_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::Targets_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::Targets_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avai_messages::msg::Targets_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avai_messages::msg::Targets_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avai_messages__msg__Targets
    std::shared_ptr<avai_messages::msg::Targets_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avai_messages__msg__Targets
    std::shared_ptr<avai_messages::msg::Targets_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Targets_ & other) const
  {
    if (this->x_position != other.x_position) {
      return false;
    }
    if (this->y_position != other.y_position) {
      return false;
    }
    if (this->round != other.round) {
      return false;
    }
    return true;
  }
  bool operator!=(const Targets_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Targets_

// alias to use template instance with default allocator
using Targets =
  avai_messages::msg::Targets_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__TARGETS__STRUCT_HPP_
