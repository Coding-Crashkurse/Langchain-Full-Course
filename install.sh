#!/bin/bash

# Installing python3
echo "Installing python3.10..."
sudo apt install python3.10 -y
echo PATH = $PATH:$HOME/.local/bin >> ~/.bashrc

# Updating pip
echo "Updating pip..."
pip3 install --upgrade pip

# Installing venv
echo "Installing Python..."
sudo apt install python3.10-venv -y

# Creating environment
echo "Creating environment..."
python3 -m venv .venv

# Activating environment
echo "Activating environment..."
source .venv/bin/activate

# Installing requirements
echo "Installing requirements..."
pip3 install -r requirements.txt
echo complete
```