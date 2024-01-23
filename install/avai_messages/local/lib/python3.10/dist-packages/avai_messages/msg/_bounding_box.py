# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avai_messages:msg/BoundingBox.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_BoundingBox(type):
    """Metaclass of message 'BoundingBox'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('avai_messages')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'avai_messages.msg.BoundingBox')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__bounding_box
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__bounding_box
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__bounding_box
            cls._TYPE_SUPPORT = module.type_support_msg__msg__bounding_box
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__bounding_box

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BoundingBox(metaclass=Metaclass_BoundingBox):
    """Message class 'BoundingBox'."""

    __slots__ = [
        '_min_x',
        '_min_y',
        '_max_x',
        '_max_y',
        '_confidence',
        '_cone',
    ]

    _fields_and_field_types = {
        'min_x': 'double',
        'min_y': 'double',
        'max_x': 'double',
        'max_y': 'double',
        'confidence': 'double',
        'cone': 'int16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.min_x = kwargs.get('min_x', float())
        self.min_y = kwargs.get('min_y', float())
        self.max_x = kwargs.get('max_x', float())
        self.max_y = kwargs.get('max_y', float())
        self.confidence = kwargs.get('confidence', float())
        self.cone = kwargs.get('cone', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.min_x != other.min_x:
            return False
        if self.min_y != other.min_y:
            return False
        if self.max_x != other.max_x:
            return False
        if self.max_y != other.max_y:
            return False
        if self.confidence != other.confidence:
            return False
        if self.cone != other.cone:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def min_x(self):
        """Message field 'min_x'."""
        return self._min_x

    @min_x.setter
    def min_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'min_x' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'min_x' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._min_x = value

    @builtins.property
    def min_y(self):
        """Message field 'min_y'."""
        return self._min_y

    @min_y.setter
    def min_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'min_y' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'min_y' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._min_y = value

    @builtins.property
    def max_x(self):
        """Message field 'max_x'."""
        return self._max_x

    @max_x.setter
    def max_x(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'max_x' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'max_x' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._max_x = value

    @builtins.property
    def max_y(self):
        """Message field 'max_y'."""
        return self._max_y

    @max_y.setter
    def max_y(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'max_y' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'max_y' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._max_y = value

    @builtins.property
    def confidence(self):
        """Message field 'confidence'."""
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'confidence' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'confidence' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._confidence = value

    @builtins.property
    def cone(self):
        """Message field 'cone'."""
        return self._cone

    @cone.setter
    def cone(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'cone' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'cone' field must be an integer in [-32768, 32767]"
        self._cone = value
