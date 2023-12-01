import rclpy
import serial
import re
import traceback
import threading

from rclpy.node import Node
from std_msgs.msg import Header
from geometry_msgs.msg import Vector3
from avai_messages.msg import Vector3Sensor, Motor, Motors, VehicleLights, Melody


class OpenCRNode(Node):

    ctr = 0
    con = None
    pub_gyro = None
    pub_accel = None
    pub_magnet = None
    pub_motor = None

    def handleInboundSerial(self):
        global con
        con.write("sound 2 1000 1 1000 1\r\n".encode("ASCII"))
        while True:
            try:
                data = con.readline()
                matcher = re.search(self.regex, data.decode("ASCII"))
                if matcher is None:
                    continue
                hdr = Header(stamp=self.get_clock().now().to_msg(),frame_id=str(self.ctr))
                accel = Vector3Sensor(header=hdr,data=Vector3(x=float(matcher.group(2)),y=float(matcher.group(3)),z=float(matcher.group(4))),update_time=int(matcher.group(1)))
                global pub_accel
                pub_accel.publish(accel)

                gyro = Vector3Sensor(header=hdr,data=Vector3(x=float(matcher.group(5)),y=float(matcher.group(6)),z=float(matcher.group(7))),update_time=int(matcher.group(1)))
                global pub_gyro
                pub_gyro.publish(gyro)

                magnet = Vector3Sensor(header=hdr,data=Vector3(x=float(matcher.group(8)),y=float(matcher.group(9)),z=float(matcher.group(10))),update_time=int(matcher.group(1)))
                global pub_magnet
                pub_magnet.publish(magnet)

                marr = []
                marr.append(Motor(position=int(matcher.group(11))))
                marr.append(Motor(position=int(matcher.group(12))))
                motors = Motors(motors=marr)
                global pub_motor
                pub_motor.publish(motors)
                global ctr
                ctr = ctr + 1
            except:
                traceback.print_exc()

    def __init__(self):
        super().__init__('opencr_node')
        global pub_gyro
        global pub_accel
        global pub_magnet
        global pub_motor
        pub_gyro = self.create_publisher(Vector3Sensor, 'gyroscope', 10)
        pub_accel = self.create_publisher(Vector3Sensor, 'accelerometer', 10)
        pub_magnet = self.create_publisher(Vector3Sensor, 'magnetometer', 10)
        pub_motor = self.create_publisher(Motors, 'motor_position', 10)

        self.motor_vel = self.create_subscription(Motors, "motor_velocity", self.handleVelocity, 10)
        self.motor_led = self.create_subscription(VehicleLights, "vehicle_led", self.handleLED, 10)
        self.opencr_sound = self.create_subscription(Melody, "sound", self.handleSound, 10)

        self.regex = r"^([0-9]+)[ \t]+([-0-9]+)[ \t]+([-0-9]+)[ \t]+([-0-9]+)[ \t]+([-0-9]+)[ \t]+([-0-9]+)[ \t]+([-0-9]+)[ \t]+([-0-9\.]+)[ \t]+([-0-9\.]+)[ \t]+([-0-9\.]+)[ \t]+([-0-9]+)[ \t]+([-0-9]+)\r\n$"

        global con
        global ctr
        con = serial.Serial('/dev/ttyACM0')
        ctr = 0


    def handleVelocity(self, msg):
        if len(msg.motors) == 2:
            con.write(("motor " + str(msg.motors[0].velocity) + " " + str(msg.motors[1].velocity) + "\r\n").encode("ASCII"))

    def handleLED(self, msg):
            con.write(("led " + str(1 if msg.left_motor else 0) + " " + str(1 if msg.right_motor else 0) + "\r\n").encode("ASCII"))

    def handleSound(self,msg):
        if len(msg.pitch) == msg.length and len(msg.duration) == msg.length:
            cmd = "sound " + str(msg.length)
            for i in range(msg.length):
                cmd = cmd + " " + str(msg.pitch[i]) + " " + str(msg.duration[i])

            con.write((cmd + "\r\n").encode("ASCII"))

def main(args=None):
    rclpy.init(args=args)

    node = OpenCRNode()
    thr = threading.Thread(target=node.handleInboundSerial)
    thr.start()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
