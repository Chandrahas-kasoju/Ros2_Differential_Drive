# Ros2_Differential_Drive
- This Repository contains a ROS2 Package for simulating a Differental Drive robot in Rviz2.
- This Package was built on Ubuntu 22.04 with ROS2 Rolling Distribution.
## Building the Package
- Make sure [ros2_control](https://github.com/ros-controls/ros2_control) and [ros2_controllers](https://github.com/ros-controls/ros2_controllers)packages are installed beforehand.
```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
https://github.com/Chandrahas-kasoju/Ros2_Differential_Drive.git
cd ~/ros2_ws
rosdep install -r --from-paths . --ignore-src --rosdistro $ROS_DISTRO -y
colcon build
```
## Simulation
- To start the simulation launch the following command
```
ros2 launch robot_bringup diff_bot.launch.py
```
- Rviv2 opens and the robot spawns in it.
- To move the root launch the following command
```
ros2 launch robot_bringup test_parameters.launch.py
```
