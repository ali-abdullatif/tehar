#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "=========================================="
echo "    Tihar Web App - VPS Setup Script"
echo "=========================================="
echo ""

echo "[1/4] Updating system packages..."
sudo apt-get update -y
sudo apt-get upgrade -y

echo "[2/4] Installing required dependencies..."
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    git \
    ufw

echo "[3/4] Installing Docker..."
# Add Docker's official GPG key:
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Set up the repository:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update -y
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Ensure docker service is running and enabled on boot
sudo systemctl enable docker
sudo systemctl start docker

echo "[4/4] Configuring Firewall (UFW)..."
# Allow OpenSSH, HTTP, and HTTPS, plus port 8000 for backend/frontend if needed directly
sudo ufw allow OpenSSH
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 8080/tcp
sudo ufw allow 8000/tcp
sudo ufw allow 8081/tcp
echo "y" | sudo ufw enable

echo ""
echo "[5/5] Cloning and Starting Application..."

# Define the repository URL
REPO_URL="https://github.com/ali-abdullatif/tehar.git"
PROJECT_DIR="tehar"

# Check if directory already exists
if [ -d "$PROJECT_DIR" ]; then
    echo "Directory $PROJECT_DIR already exists. Pulling latest changes..."
    cd $PROJECT_DIR
    git pull
else
    echo "Cloning repository..."
    git clone $REPO_URL
    cd $PROJECT_DIR
fi

echo "Building and starting Docker containers..."
sudo docker compose up --build -d

echo ""
echo "=========================================="
echo "    VPS Setup Completed Successfully!"
echo "=========================================="
echo "Your application should now be running."
