import rclpy
import rclpy.node
from rcl_interfaces.msg import ParameterDescriptor
from geometry_msgs.msg import Twist


class VelParam(rclpy.node.Node):
    def __init__(self):
        super().__init__('param_vel_node')
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.publisher = self.create_publisher(Twist, '/diffbot_base_controller/cmd_vel_unstamped', 10)
        self.msg = Twist()
        param_descriptor = ParameterDescriptor(
            description='Sets the velocity (in m/s) of the robot.')
        self.declare_parameter('velocity_x', 0.0, param_descriptor)
        self.declare_parameter('angular_z', 0.0, param_descriptor)
        # self.add_on_set_parameters_callback(self.parameter_callback)

    def timer_callback(self):
        my_param_x = self.get_parameter('velocity_x').value
        my_param_y = self.get_parameter('angular_z').value

        self.get_logger().info('Velocity parameter is: %f' % my_param_x)

        self.msg.linear.x = my_param_x
        self.msg.angular.z = my_param_y
        self.publisher.publish(self.msg)

    # def parameter_callback(self, params):
    #     for param in params:
    #         if param.name == 'velocity' and param.type_ == Parameter.Type.DOUBLE:
    #             self.my_param = param.value
    #             self.get_logger().info('Velocity parameter changed!')
    #     return SetParametersResult(successful=True)

def main():
    rclpy.init()
    node = VelParam()
    rclpy.spin(node)


if __name__ == '__main__':
    main()
