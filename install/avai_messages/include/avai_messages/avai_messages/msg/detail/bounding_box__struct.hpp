// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avai_messages:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__STRUCT_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__avai_messages__msg__BoundingBox __attribute__((deprecated))
#else
# define DEPRECATED__avai_messages__msg__BoundingBox __declspec(deprecated)
#endif

namespace avai_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct BoundingBox_
{
  using Type = BoundingBox_<ContainerAllocator>;

  explicit BoundingBox_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->min_x = 0.0;
      this->min_y = 0.0;
      this->max_x = 0.0;
      this->max_y = 0.0;
      this->confidence = 0.0;
      this->cone = 0;
    }
  }

  explicit BoundingBox_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->min_x = 0.0;
      this->min_y = 0.0;
      this->max_x = 0.0;
      this->max_y = 0.0;
      this->confidence = 0.0;
      this->cone = 0;
    }
  }

  // field types and members
  using _min_x_type =
    double;
  _min_x_type min_x;
  using _min_y_type =
    double;
  _min_y_type min_y;
  using _max_x_type =
    double;
  _max_x_type max_x;
  using _max_y_type =
    double;
  _max_y_type max_y;
  using _confidence_type =
    double;
  _confidence_type confidence;
  using _cone_type =
    int16_t;
  _cone_type cone;

  // setters for named parameter idiom
  Type & set__min_x(
    const double & _arg)
  {
    this->min_x = _arg;
    return *this;
  }
  Type & set__min_y(
    const double & _arg)
  {
    this->min_y = _arg;
    return *this;
  }
  Type & set__max_x(
    const double & _arg)
  {
    this->max_x = _arg;
    return *this;
  }
  Type & set__max_y(
    const double & _arg)
  {
    this->max_y = _arg;
    return *this;
  }
  Type & set__confidence(
    const double & _arg)
  {
    this->confidence = _arg;
    return *this;
  }
  Type & set__cone(
    const int16_t & _arg)
  {
    this->cone = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avai_messages::msg::BoundingBox_<ContainerAllocator> *;
  using ConstRawPtr =
    const avai_messages::msg::BoundingBox_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avai_messages::msg::BoundingBox_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avai_messages::msg::BoundingBox_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::BoundingBox_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::BoundingBox_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::BoundingBox_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::BoundingBox_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avai_messages::msg::BoundingBox_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avai_messages::msg::BoundingBox_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avai_messages__msg__BoundingBox
    std::shared_ptr<avai_messages::msg::BoundingBox_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avai_messages__msg__BoundingBox
    std::shared_ptr<avai_messages::msg::BoundingBox_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const BoundingBox_ & other) const
  {
    if (this->min_x != other.min_x) {
      return false;
    }
    if (this->min_y != other.min_y) {
      return false;
    }
    if (this->max_x != other.max_x) {
      return false;
    }
    if (this->max_y != other.max_y) {
      return false;
    }
    if (this->confidence != other.confidence) {
      return false;
    }
    if (this->cone != other.cone) {
      return false;
    }
    return true;
  }
  bool operator!=(const BoundingBox_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct BoundingBox_

// alias to use template instance with default allocator
using BoundingBox =
  avai_messages::msg::BoundingBox_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__BOUNDING_BOX__STRUCT_HPP_
