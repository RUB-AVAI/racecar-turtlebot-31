// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avai_messages:msg/ClusteredLidarData.idl
// generated code does not contain a copyright notice

#ifndef AVAI_MESSAGES__MSG__DETAIL__CLUSTERED_LIDAR_DATA__STRUCT_HPP_
#define AVAI_MESSAGES__MSG__DETAIL__CLUSTERED_LIDAR_DATA__STRUCT_HPP_

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
// Member 'clusters'
#include "avai_messages/msg/detail/cluster__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__avai_messages__msg__ClusteredLidarData __attribute__((deprecated))
#else
# define DEPRECATED__avai_messages__msg__ClusteredLidarData __declspec(deprecated)
#endif

namespace avai_messages
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ClusteredLidarData_
{
  using Type = ClusteredLidarData_<ContainerAllocator>;

  explicit ClusteredLidarData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    (void)_init;
  }

  explicit ClusteredLidarData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _clusters_type =
    std::vector<avai_messages::msg::Cluster_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<avai_messages::msg::Cluster_<ContainerAllocator>>>;
  _clusters_type clusters;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__clusters(
    const std::vector<avai_messages::msg::Cluster_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<avai_messages::msg::Cluster_<ContainerAllocator>>> & _arg)
  {
    this->clusters = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avai_messages::msg::ClusteredLidarData_<ContainerAllocator> *;
  using ConstRawPtr =
    const avai_messages::msg::ClusteredLidarData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avai_messages::msg::ClusteredLidarData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avai_messages::msg::ClusteredLidarData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::ClusteredLidarData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::ClusteredLidarData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avai_messages::msg::ClusteredLidarData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avai_messages::msg::ClusteredLidarData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avai_messages::msg::ClusteredLidarData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avai_messages::msg::ClusteredLidarData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avai_messages__msg__ClusteredLidarData
    std::shared_ptr<avai_messages::msg::ClusteredLidarData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avai_messages__msg__ClusteredLidarData
    std::shared_ptr<avai_messages::msg::ClusteredLidarData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ClusteredLidarData_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->clusters != other.clusters) {
      return false;
    }
    return true;
  }
  bool operator!=(const ClusteredLidarData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ClusteredLidarData_

// alias to use template instance with default allocator
using ClusteredLidarData =
  avai_messages::msg::ClusteredLidarData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avai_messages

#endif  // AVAI_MESSAGES__MSG__DETAIL__CLUSTERED_LIDAR_DATA__STRUCT_HPP_
