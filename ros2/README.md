# ROS2 Jazzy + Gazebo Harmonic Setup

**Ubuntu 24.04 (Noble) | ROS2 Jazzy Jalisco (LTS) | Gazebo Harmonic (LTS)**

---

## 📦 Installed Packages

### ROS2 Core (via `ros-jazzy-desktop`)
- `ros-jazzy-desktop` - RViz2, rqt, basic simulation tools
- `ros-jazzy-ros-core` - Core ROS2 libraries
- `ros-jazzy-ros-base` - Base ROS2 packages
- `ros-dev-tools` - Development tools (colcon, rosdep, vcstool)

### Gazebo Harmonic
- `gz-harmonic` - Gazebo Sim 8.x (Harmonic LTS)
- `gz-sim8`, `gz-transport13`, `gz-msgs10`, `gz-physics7`, `gz-rendering8`, `gz-sensors8`, `gz-gui8`

### ROS2 ↔ Gazebo Integration
- `ros-jazzy-ros-gz` - Meta-package for ROS-Gazebo interfaces
- `ros-jazzy-ros-gz-bridge` - ROS-Gazebo message bridge
- `ros-jazzy-ros-gz-sim` - Gazebo simulation integration
- `ros-jazzy-ros-gz-image` - Image transport bridge
- `ros-jazzy-ros-gz-sim-demos` - Demo worlds

### Navigation & SLAM
- `ros-jazzy-nav2-bringup` - Nav2 stack (planner, controller, behavior tree)
- `ros-jazzy-slam-toolbox` - SLAM Toolbox (mapping & localization)
- All Nav2 sub-packages: amcl, bt-navigator, controller, costmap-2d, planner, smoother, etc.

### ROS2 Control
- `ros-jazzy-ros2-control` - Controller manager, hardware interface
- `ros-jazzy-ros2-controllers` - All standard controllers (diff-drive, joint-trajectory, PID, etc.)
- `ros-jazzy-gz-ros2-control` - Gazebo hardware plugins for ros2_control

### Robot Description & Visualization
- `ros-jazzy-robot-state-publisher` - URDF → TF publisher
- `ros-jazzy-xacro` - XML macro processor for URDF
- `ros-jazzy-joint-state-publisher-gui` - Joint state GUI

---

## 📁 Directory Structure

```
~/my_learnings/ros2/
├── core/               # Core concepts notes
├── installation/       # Installation logs & scripts
├── launch/             # Custom launch files
├── packages/           # Reference packages
├── projects/           # Your projects
├── tf2/                # TF2 learning materials
├── urdf/               # URDF models
└── ws/                 # Colcon Workspace
    ├── build/
    ├── install/
    ├── log/
    └── src/            # YOUR PACKAGES GO HERE
        ├── my_robot_description/
        ├── my_robot_bringup/
        └── my_robot_control/
```

---

## 🔧 Environment Setup

### Sourced Files (in `~/.bashrc`)

```bash
# ROS2 Jazzy Jalisco
source /opt/ros/jazzy/setup.bash

# Gazebo Harmonic (no setup.bash needed - uses pkg-config)
# Gazebo commands work directly after installation

# Local Workspace
source ~/my_learnings/ros2/ws/install/setup.bash
```

### Useful Aliases (in `~/.bashrc`)

| Alias | Command |
|-------|---------|
| `cb` | Build workspace (`colcon build --symlink-install`) |
| `cbc` | Build Release mode |
| `cbct` | Build + run tests |
| `ros2doctor` | Run `ros2 doctor` |
| `gzsim` | Run `gz sim` |
| `gzsimv` | Run `gz sim -v 4` (verbose) |
| `src` | Reload `.bashrc` |
| `rosws` | `cd ~/my_learnings/ros2/ws` |
| `rossrc` | `cd ~/my_learnings/ros2/ws/src` |

---

## ✅ Verification Commands

```bash
# Check ROS2 installation
ros2 doctor

# Check Gazebo version
gz sim --version

# Test ROS2 pub/sub
ros2 run demo_nodes_cpp talker &
ros2 run demo_nodes_cpp listener

# Test ROS2-Gazebo bridge
ros2 launch ros_gz_sim gz_sim.launch.py

# List ROS2 packages
ros2 pkg list | grep -E "(nav2|slam|control|gz)"

# Check rosdep
rosdep resolve nav2_bringup
```

---

## 🚀 Quick Start: Create a Package

```bash
cd ~/my_learnings/ros2/ws/src

# C++ package
ros2 pkg create --build-type ament_cmake my_cpp_pkg --dependencies rclcpp std_msgs

# Python package
ros2 pkg create --build-type ament_python my_py_pkg --dependencies rclpy std_msgs

# Build
cb
```

---

## 📚 Key Package Locations

| Component | Install Path |
|-----------|--------------|
| ROS2 Jazzy | `/opt/ros/jazzy/` |
| Gazebo Harmonic | `/usr/lib/x86_64-linux-gnu/gz/`, `/usr/share/gz/` |
| Gazebo Models | `~/.gz/models/` or `/usr/share/gz/gz-sim8/` |
| Workspace Install | `~/my_learnings/ros2/ws/install/` |

---

## 🔍 Troubleshooting

### ROS2 not found
```bash
source /opt/ros/jazzy/setup.bash
source ~/my_learnings/ros2/ws/install/setup.bash
```

### Gazebo not finding plugins
```bash
export GZ_SIM_SYSTEM_PLUGIN_PATH=/opt/ros/jazzy/lib:$GZ_SIM_SYSTEM_PLUGIN_PATH
```

### rosdep errors
```bash
rosdep update
rosdep install --from-paths src --ignore-src -r -y
```

### Build failures
```bash
cd ~/my_learnings/ros2/ws
rm -rf build install log
cb
```

---

## 📖 Learning Resources

- [ROS2 Jazzy Docs](https://docs.ros.org/en/jazzy/)
- [Gazebo Harmonic Docs](https://gazebosim.org/docs/harmonic)
- [Nav2 Docs](https://navigation.ros.org/)
- [ROS2 Control Docs](https://control.ros.org/)
- [SLAM Toolbox](https://github.com/SteveMacenski/slam_toolbox)

---

## 📝 Installation Log

**Date**: $(date)
**Ubuntu**: 24.04 Noble
**Kernel**: 7.0.0-28-generic
**ROS2**: Jazzy Jalisco (via apt)
**Gazebo**: Harmonic 8.x (via apt)
**Workspace**: `~/my_learnings/ros2/ws`

### Apt Packages Installed
```
ros-jazzy-desktop
gz-harmonic
ros-jazzy-ros-gz
ros-jazzy-nav2-bringup
ros-jazzy-slam-toolbox
ros-jazzy-ros2-control
ros-jazzy-ros2-controllers
ros-jazzy-gz-ros2-control
ros-jazzy-robot-state-publisher
ros-jazzy-xacro
ros-jazzy-joint-state-publisher-gui
ros-dev-tools
python3-colcon-common-extensions
python3-rosdep
python3-vcstool
```

---

*Generated automatically during setup*