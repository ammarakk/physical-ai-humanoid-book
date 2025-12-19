# Gazebo Physics Simulation Example

This script provides a basic example of interacting with Gazebo for physics simulation. It demonstrates how to launch a Gazebo world and interact with a simulated robot (e.g., publishing commands, reading sensor data).

```python
import rclpy
from rclpy.node import Node
from gazebo_msgs.srv import SpawnEntity, DeleteEntity
from geometry_msgs.msg import Pose

class GazeboSimulationClient(Node):
    def __init__(self):
        super().__init__('gazebo_simulation_client')
        self.spawn_client = self.create_client(SpawnEntity, 'spawn_entity')
        self.delete_client = self.create_client(DeleteEntity, 'delete_entity')

        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('spawn_entity service not available, waiting again...')
        while not self.delete_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('delete_entity service not available, waiting again...')

        self.get_logger().info('Gazebo simulation client ready.')

    def spawn_robot(self, name, xml_path, x=0.0, y=0.0, z=0.0):
        # Placeholder for robot XML content
        with open(xml_path, 'r') as f:
            robot_xml = f.read()

        request = SpawnEntity.Request()
        request.name = name
        request.xml = robot_xml
        request.robot_namespace = name
        request.initial_pose = Pose()
        request.initial_pose.position.x = x
        request.initial_pose.position.y = y
        request.initial_pose.position.z = z

        self.get_logger().info(f'Spawning entity: {name}')
        future = self.spawn_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info(f'Spawn result: {future.result().status_message}')
        else:
            self.get_logger().error('Service call failed %r' % (future.exception(),))

    def delete_robot(self, name):
        request = DeleteEntity.Request()
        request.name = name
        self.get_logger().info(f'Deleting entity: {name}')
        future = self.delete_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        if future.result() is not None:
            self.get_logger().info(f'Delete result: {future.result().status_message}')
        else:
            self.get_logger().error('Service call failed %r' % (future.exception(),))

def main(args=None):
    rclpy.init(args=args)
    client = GazeboSimulationClient()

    # Example: Spawn a simple box (you'd replace box.xml with your robot model)
    # This assumes 'box.xml' is available or you provide a full path to a valid URDF/SDF
    # For a real humanoid, you would load its specific URDF/SDF XML
    # client.spawn_robot('my_humanoid', 'path/to/humanoid.urdf', 0.0, 0.0, 1.0)
    # time.sleep(5) # Simulate some time running
    # client.delete_robot('my_humanoid')

    client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

# TODO: Expand this Gazebo simulation example to include a full humanoid robot model,
# demonstrate publishing joint commands, reading sensor data, and implementing basic control loops.
# Ensure the example is reproducible and clearly explains setup steps (e.g., installing Gazebo,
# sourcing robot models).
```