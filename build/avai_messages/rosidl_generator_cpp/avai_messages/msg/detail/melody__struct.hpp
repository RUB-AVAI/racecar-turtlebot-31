// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avai_messages:msg/Melody.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__MELODY__STRUCT_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__MELODY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__avai_messages__msg__Melody __attribute__((deprecated))
#else
# define DEPRECATED__avai_messages__msg__Melody __declspec(deprecated)
#endif

namespace avai_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Melody_
{
  using Type = Melody_<ContainerAllocator>;

  explicit Melody_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->length = 0;
    }
  }

  explicit Melody_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->length = 0;
    }
  }

  // field types and members
  using _length_type =
    uint8_t;
  _length_type length;
  using _pitch_type =
    std::vector<uint16_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint16_t>>;
  _pitch_type pitch;
  using _duration_type =
    std::vector<uint16_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint16_t>>;
  _duration_type duration;

  // setters for named parameter idiom
  Type & set__length(
    const uint8_t & _arg)
  {
    this->length = _arg;
    return *this;
  }
  Type & set__pitch(
    const std::vector<uint16_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint16_t>> & _arg)
  {
    this->pitch = _arg;
    return *this;
  }
  Type & set__duration(
    const std::vector<uint16_t, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<uint16_t>> & _arg)
  {
    this->duration = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avai_messages::msg::Melody_<ContainerAllocator> *;
  using ConstRawPtr =
    const avai_messages::msg::Melody_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avai_messages::msg::Melody_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avai_messages::msg::Melody_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::Melody_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::Melody_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::Melody_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::Melody_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avai_messages::msg::Melody_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avai_messages::msg::Melody_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avai_messages__msg__Melody
    std::shared_ptr<avai_messages::msg::Melody_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avai_messages__msg__Melody
    std::shared_ptr<avai_messages::msg::Melody_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Melody_ & other) const
  {
    if (this->length != other.length) {
      return false;
    }
    if (this->pitch != other.pitch) {
      return false;
    }
    if (this->duration != other.duration) {
      return false;
    }
    return true;
  }
  bool operator!=(const Melody_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Melody_

// alias to use template instance with default allocator
using Melody =
  avai_messages::msg::Melody_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__MELODY__STRUCT_HPP_
