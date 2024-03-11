# generated from rosidl_generator_py/resource/_idl.py.em
# with input from avai_messages:msg/Targets.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Targets(type):
    """Metaclass of message 'Targets'."""

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
                'avai_messages.msg.Targets')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__targets
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__targets
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__targets
            cls._TYPE_SUPPORT = module.type_support_msg__msg__targets
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__targets

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Targets(metaclass=Metaclass_Targets):
    """Message class 'Targets'."""

    __slots__ = [
        '_x_position',
        '_y_position',
        '_round',
    ]

    _fields_and_field_types = {
        'x_position': 'double',
        'y_position': 'double',
        'round': 'int8',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.x_position = kwargs.get('x_position', float())
        self.y_position = kwargs.get('y_position', float())
        self.round = kwargs.get('round', int())

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
        if self.x_position != other.x_position:
            return False
        if self.y_position != other.y_position:
            return False
        if self.round != other.round:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def x_position(self):
        """Message field 'x_position'."""
        return self._x_position

    @x_position.setter
    def x_position(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'x_position' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'x_position' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._x_position = value

    @builtins.property
    def y_position(self):
        """Message field 'y_position'."""
        return self._y_position

    @y_position.setter
    def y_position(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'y_position' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'y_position' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._y_position = value

    @builtins.property  # noqa: A003
    def round(self):  # noqa: A003
        """Message field 'round'."""
        return self._round

    @round.setter  # noqa: A003
    def round(self, value):  # noqa: A003
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'round' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'round' field must be an integer in [-128, 127]"
        self._round = value
