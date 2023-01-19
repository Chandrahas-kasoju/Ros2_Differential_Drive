from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    config = os.path.join(
        get_package_share_directory('robot_bringup'),
        'config',
        'param_vel_node.yaml'
        )
    return LaunchDescription([
        Node(
            package='ros2_control_tests_nodes',
            executable='vel_pub',
            name='param_vel_node',
            output='screen',
            emulate_tty=True,
            parameters=[config]
        )
    ])
