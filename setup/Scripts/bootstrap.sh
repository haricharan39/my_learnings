#!/usr/bin/env bash
set -e

echo "===== Updating System ====="
sudo apt update
sudo apt upgrade -y

echo "===== Installing Development Tools ====="
sudo apt install -y \
git curl wget vim nano tree htop btop \
unzip zip build-essential cmake pkg-config \
software-properties-common python3 python3-pip \
python3-venv python3-dev \
clang clang-format gdb valgrind ninja-build \
ccache graphviz doxygen \
tmux fzf ripgrep fd-find jq \
docker.io docker-compose-v2 \
nodejs npm

echo "===== Creating Learning Directories ====="
mkdir -p ~/my_learnings

echo "===== Done ====="
echo "Now install:"
echo "  • ROS 2 Jazzy"
echo "  • Webots"
echo "  • Foxglove Studio"
echo "  • NVIDIA CUDA Toolkit (if needed)"
echo "  • PyTorch"