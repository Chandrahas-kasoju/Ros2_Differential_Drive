from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_control_tests_nodes',
            executable='vel_pub',
            name='vel_pub',
            output='screen',
            emulate_tty=True,
            parameters=[
                {'velocity_x': 0.2}
            ]
        )
    ])
