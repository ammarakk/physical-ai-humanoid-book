# ROS 2: The Robotic Nervous System

This chapter will introduce ROS 2 (Robot Operating System 2) as the foundational "nervous system" for humanoid robots. It will cover the core concepts and components necessary to build and manage a robotic software architecture.

## Key Topics:
- ROS 2 Nodes, Topics, Services, Actions
- URDF for humanoid robot descriptions
- Using rclpy for Python-based ROS 2 agents
- Launch files, parameters, and controllers

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

```

![ROS 2 Command Flow Diagram](static/img/ros2-command-flow.svg)

<!-- TODO: Please fill in the detailed content for this chapter, including explanations, examples, and relevant research. Ensure all claims are supported by APA 7th edition citations. -->