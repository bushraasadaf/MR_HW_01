import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class SubscriberNode(Node):
    def __init__(self): 
        super().__init__('subscriber_node')
        self.subscriber_ = self.create_subscription(String,'char_topic',self.get_message,10)
    #function for received msgs
    def get_message(self,msg):
        self.get_logger().info('Message received: "%s"' % msg.data)
    

def main(args=None):
    rclpy.init(args=args)
    node_subscriber = SubscriberNode()
    try:
        #keep node running
        rclpy.spin(node_subscriber)
    except KeyboardInterrupt:
        pass
    node_subscriber.destroy_node()
    if rclpy.ok():
        rclpy.shutdown()
    

if __name__ == '__main__':
    main()
        