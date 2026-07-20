# ROS 2 Jazzy Installation Guide

## System Information

- OS: Ubuntu 24.04 LTS (Noble Numbat)
- Architecture: x86_64
- User: hari39
- Computer Name: cosmos

---

## Prerequisites

Update the system:

```bash
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
```

Install basic development tools:

```bash
sudo apt install -y \
build-essential \
cmake \
git \
curl \
wget \
python3-pip \
python3-venv
```

---

## ROS 2 Installation

Official documentation:

https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html

Installation date:

```
YYYY-MM-DD
```

Installed packages:

- ros-jazzy-desktop
- colcon
- rosdep
- vcstool

---

## Environment Setup

Source ROS 2:

```bash
source /opt/ros/jazzy/setup.bash
```

Permanent setup:

```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
```

Reload:

```bash
source ~/.bashrc
```

---

## Workspace

Workspace location:

```
~/my_learnings/ros2/Projects/ros2_ws
```

Create workspace:

```bash
mkdir -p ~/my_learnings/ros2/Projects/ros2_ws/src
```

Build:

```bash
cd ~/my_learnings/ros2/Projects/ros2_ws
colcon build
```

Source workspace:

```bash
source install/setup.bash
```

---

## Verification

ROS version:

```bash
ros2 --version
```

Topics:

```bash
ros2 topic list
```

Packages:

```bash
ros2 pkg list
```

---

## Troubleshooting

### Problem:

Solution:

---

## Notes

(Add your own notes here.)
