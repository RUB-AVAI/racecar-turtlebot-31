// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avai_messages:msg/YoloOutput.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__YOLO_OUTPUT__STRUCT_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__YOLO_OUTPUT__STRUCT_HPP_

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
// Member 'bounding_boxes'
#include "avai_messages/msg/detail/bounding_box__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__avai_messages__msg__YoloOutput __attribute__((deprecated))
#else
# define DEPRECATED__avai_messages__msg__YoloOutput __declspec(deprecated)
#endif

namespace avai_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct YoloOutput_
{
  using Type = YoloOutput_<ContainerAllocator>;

  explicit YoloOutput_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    (void)_init;
  }

  explicit YoloOutput_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _bounding_boxes_type =
    std::vector<avai_messages::msg::BoundingBox_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<avai_messages::msg::BoundingBox_<ContainerAllocator>>>;
  _bounding_boxes_type bounding_boxes;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__bounding_boxes(
    const std::vector<avai_messages::msg::BoundingBox_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<avai_messages::msg::BoundingBox_<ContainerAllocator>>> & _arg)
  {
    this->bounding_boxes = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avai_messages::msg::YoloOutput_<ContainerAllocator> *;
  using ConstRawPtr =
    const avai_messages::msg::YoloOutput_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avai_messages::msg::YoloOutput_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avai_messages::msg::YoloOutput_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::YoloOutput_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::YoloOutput_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::YoloOutput_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::YoloOutput_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avai_messages::msg::YoloOutput_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avai_messages::msg::YoloOutput_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avai_messages__msg__YoloOutput
    std::shared_ptr<avai_messages::msg::YoloOutput_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avai_messages__msg__YoloOutput
    std::shared_ptr<avai_messages::msg::YoloOutput_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const YoloOutput_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->bounding_boxes != other.bounding_boxes) {
      return false;
    }
    return true;
  }
  bool operator!=(const YoloOutput_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct YoloOutput_

// alias to use template instance with default allocator
using YoloOutput =
  avai_messages::msg::YoloOutput_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__YOLO_OUTPUT__STRUCT_HPP_
