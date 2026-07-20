#!/usr/bin/env bash

echo "========== SYSTEM =========="
hostnamectl

echo
echo "========== CPU =========="
lscpu | grep "Model name"

echo
echo "========== MEMORY =========="
free -h

echo
echo "========== GPU =========="
nvidia-smi

echo
echo "========== DISK =========="
df -h /

echo
echo "========== VERSIONS =========="
git --version
python3 --version
webots --version
docker --version
node --version
code --version