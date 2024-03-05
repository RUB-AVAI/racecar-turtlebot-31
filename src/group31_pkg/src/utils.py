def get_timestamp_as_float(msg):
    return msg.header.stamp.sec + msg.header.stamp.nanosec / 1e9