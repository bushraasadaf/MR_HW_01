import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class CosineWave(Node):
    def __init__(self):
        super().__init__('cosine_node')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.timer_period = 0.1  #publish loop rate of 10 Hz
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.t = 0.0 
        self.A = 1.0 #amplitude 
        self.k = 3.0 #kept this greater than 1 to create more wave cycles 

    def timer_callback(self):
        A = self.A
        k = self.k
        t = self.t

        v = math.sqrt(1 + (A * k * math.sin(k * t)) ** 2)
        omega = (-A * k**2 * math.cos(k * t)) / (1 + (A * k * math.sin(k * t)) ** 2)

        msg = Twist()
        msg.linear.x = v
        msg.angular.z = omega
        self.publisher_.publish(msg)

        self.t += self.timer_period

def main(args=None):
    rclpy.init(args=args)
    node = CosineWave()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    if rclpy.ok():
        rclpy.shutdown()


if __name__ == '__main__':
    main()