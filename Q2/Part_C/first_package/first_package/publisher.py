import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        self.publisher_ = self.create_publisher(String,'char_topic',10)
    
    def publish_message(self):  #this takes input from user and publishes it to the topic
        user_input = input("Enter a message to publish: ")
        msg = String() #string message object
        msg.data = user_input #data field of the message obj is set to user input

        self.publisher_.publish(msg)

def main(args=None):
        rclpy.init(args=args)
        node_publisher = PublisherNode()
        try:
            while rclpy.ok():
                node_publisher.publish_message()
        except KeyboardInterrupt:
            pass    
        node_publisher.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()

if __name__ == '__main__':
    main()

            

