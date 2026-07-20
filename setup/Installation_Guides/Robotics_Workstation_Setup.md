# Robotics & AI Development Workstation Setup

**Author:** Hari Charan
**OS:** Ubuntu 24.04 LTS (Noble Numbat)
**Hostname:** cosmos
**User:** hari39

---

# 1. System Information

```bash
lsb_release -a
uname -r
hostnamectl
```

---

# 2. System Update

```bash
sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y
```

---

# 3. Essential Development Tools

```bash
sudo apt install -y \
git \
curl \
wget \
vim \
nano \
tree \
htop \
btop \
unzip \
zip \
build-essential \
cmake \
pkg-config \
software-properties-common \
python3 \
python3-pip \
python3-venv \
python3-dev
```

Verify:

```bash
git --version
python3 --version
```

---

# 4. Git Configuration

```bash
git config --global user.name "Hari Charan"
git config --global user.email "YOUR_EMAIL"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
```

Check:

```bash
git config --global --list
```

---

# 5. GitHub SSH

Generate key:

```bash
ssh-keygen -t ed25519 -C "YOUR_EMAIL"
```

Display public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Add the key to:

https://github.com/settings/keys

Test:

```bash
ssh -T git@github.com
```

Expected:

```
Hi <username>! You've successfully authenticated...
```

---

# 6. Visual Studio Code

Install:

```bash
sudo snap install code --classic
```

Recommended Extensions:

- Python
- Pylance
- C/C++
- CMake Tools
- ROS
- GitLens
- Docker
- Material Icon Theme
- Tokyo Night
- Error Lens
- Markdown All in One

---

# 7. ROS 2 Jazzy

Official Guide:

https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html

Verify:

```bash
source /opt/ros/jazzy/setup.bash
ros2 pkg list | head
```

---

# 8. ROS 2 Workspace

Workspace:

```
~/my_learnings/ros2/Projects/ros2_ws
```

Create:

```bash
mkdir -p ~/my_learnings/ros2/Projects/ros2_ws/src
```

Build:

```bash
cd ~/my_learnings/ros2/Projects/ros2_ws
colcon build
```

Add to bashrc:

```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
echo "source ~/my_learnings/ros2/Projects/ros2_ws/install/setup.bash" >> ~/.bashrc
```

Reload:

```bash
source ~/.bashrc
```

---

# 9. Webots

Install:

```bash
sudo snap install webots
```

Verify:

```bash
webots
```

Version:

```
R2025a
```

Workspace:

```
~/my_learnings/webots/Projects/workspace
```

---

# 10. Foxglove Studio

Download:

https://foxglove.dev/download

Install:

```bash
sudo apt install ./foxglove-studio-*.deb
```

Launch:

```bash
foxglove-studio
```

---

# 11. Python Virtual Environment

Create:

```bash
mkdir -p ~/my_learnings/ai_ml/.venvs

python3 -m venv \
~/my_learnings/ai_ml/.venvs/robotics
```

Activate:

```bash
source \
~/my_learnings/ai_ml/.venvs/robotics/bin/activate
```

Upgrade:

```bash
pip install --upgrade pip setuptools wheel
```

---

# 12. Scientific Python Stack

```bash
pip install \
numpy \
scipy \
pandas \
matplotlib \
opencv-python \
opencv-contrib-python \
scikit-learn \
jupyterlab \
ipython \
notebook \
pyyaml
```

Verify:

```bash
python -c \
"import cv2,numpy,pandas,matplotlib"
```

---

# 13. PyTorch (CUDA)

Install using the command from:

https://pytorch.org/get-started/locally/

Verify:

```bash
python -c "import torch; print(torch.__version__)"
python -c "import torch; print(torch.cuda.is_available())"
```

Expected:

```
True
```

---

# 14. NVIDIA

Check:

```bash
nvidia-smi
```

Current GPU:

- NVIDIA GeForce RTX 4050
- CUDA Enabled

---

# 15. Docker

Install:

```bash
sudo apt install -y docker.io docker-compose-v2
sudo usermod -aG docker $USER
```

Verify:

```bash
docker --version
docker compose version
```

---

# 16. Development Utilities

```bash
sudo apt install -y \
tmux \
fzf \
ripgrep \
fd-find \
jq \
clang \
clang-format \
gdb \
valgrind \
ninja-build \
ccache \
graphviz \
doxygen
```

---

# 17. Node.js

```bash
sudo apt install -y nodejs npm
```

Verify:

```bash
node --version
npm --version
```

---

# 18. Directory Layout

```
my_learnings/
├── setup/
├── foundations/
├── programming/
├── linux/
├── git_github/
├── robotics/
├── ros2/
├── webots/
├── slam/
├── navigation/
├── computer_Vision/
├── ai_ml/
├── reinforcement_learning/
├── embedded_Systems/
├── cuda_gpu/
├── cybersecurity/
├── cloud_DevOps/
├── mechanical/
├── projects/
├── research/
├── career/
├── books/
├── courses/
├── notes/
├── resources/
├── scripts/
├── tools/
└── archive/
```

---

# 19. Verification

```bash
git --version
python3 --version
ros2 pkg list | head
webots --version
docker --version
node --version
code --version
nvidia-smi
```

---

# 20. Learning Roadmap

1. Linux
2. Git & GitHub
3. Python
4. C++
5. ROS 2
6. Webots
7. URDF
8. TF2
9. SLAM
10. Navigation (Nav2)
11. OpenCV
12. PyTorch
13. Reinforcement Learning
14. Multi-Robot Systems
15. Embedded Systems
16. Real Robot Deployment

---

# Notes

- Keep projects inside `~/my_learnings`.
- Use Python virtual environments for AI/ML projects.
- Update packages regularly.
- Commit projects to GitHub frequently.
- Document each project with a README.