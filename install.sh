#!/bin/bash

# ============================================
# IGAS - Automated Installation Script
# For Termux and Linux Systems
# ============================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "${BLUE}════════════════════════════════════════${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}════════════════════════════════════════${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# Main Installation
print_header "IGAS Installation Started"

# Check if running on Termux or Linux
if [ -d "/data/data/com.termux" ]; then
    print_info "Detected: Termux Environment"
    IS_TERMUX=true
else
    print_info "Detected: Linux/Unix Environment"
    IS_TERMUX=false
fi

# Step 1: Update System
print_header "Step 1: Updating System"
if [ "$IS_TERMUX" = true ]; then
    pkg update -y && pkg upgrade -y
else
    sudo apt update && sudo apt upgrade -y
fi
print_success "System updated"

# Step 2: Install System Dependencies
print_header "Step 2: Installing System Dependencies"

if [ "$IS_TERMUX" = true ]; then
    pkg install python3 python3-pip git curl wget -y
    pkg install libffi-dev libssl-dev build-essential -y
else
    sudo apt install python3 python3-pip python3-dev python3-venv -y
    sudo apt install build-essential libssl-dev libffi-dev git curl wget -y
fi
print_success "System dependencies installed"

# Step 3: Check Python Version
print_header "Step 3: Checking Python Version"
PYTHON_VERSION=$(python3 --version | awk '{print $2}')
print_info "Python version: $PYTHON_VERSION"

if ! python3 -c 'import sys; exit(0 if sys.version_info >= (3, 8) else 1)'; then
    print_error "Python 3.8+ required!"
    exit 1
fi
print_success "Python version check passed"

# Step 4: Create Virtual Environment (Optional)
print_header "Step 4: Setting Up Python Environment"
read -p "Create virtual environment? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python3 -m venv venv
    source venv/bin/activate
    print_success "Virtual environment created"
else
    print_warning "Skipping virtual environment"
fi

# Step 5: Install Python Requirements
print_header "Step 5: Installing Python Requirements"
print_info "This may take a few minutes..."

pip3 install --upgrade pip setuptools wheel
pip3 install -r requirements.txt

print_success "Python requirements installed"

# Step 6: Create Project Structure
print_header "Step 6: Creating Project Structure"

mkdir -p instagram-tools/{auto_poster,bot,reporter}
mkdir -p termux-bot/{system_monitor,task_scheduler,notification}
mkdir -p web-app/{backend,frontend,database}
mkdir -p cli-tools/{file_manager,data_converter,batch_processor}
mkdir -p scrapers/{instagram_scraper,web_scraper,api_scraper}
mkdir -p shared/{config,utils,modules}
mkdir -p docs
mkdir -p logs
mkdir -p data
mkdir -p cache
mkdir -p results

print_success "Project structure created"

# Step 7: Create __init__.py files
print_header "Step 7: Creating Python Package Structures"

for dir in instagram-tools/{auto_poster,bot,reporter} \
           termux-bot/{system_monitor,task_scheduler,notification} \
           cli-tools/{file_manager,data_converter,batch_processor} \
           scrapers/{instagram_scraper,web_scraper,api_scraper} \
           shared/{config,utils,modules}; do
    touch "$dir/__init__.py"
done

print_success "Package structures created"

# Step 8: Setup Configuration
print_header "Step 8: Setting Up Configuration"

if [ ! -f ".env" ]; then
    cp config/.env.example .env
    print_info "Created .env file from template"
    print_warning "IMPORTANT: Edit .env file with your credentials!"
    print_warning "  nano .env"
else
    print_info ".env file already exists"
fi

# Step 9: Create Essential Files
print_header "Step 9: Creating Essential Support Files"

# Create __init__.py for main packages
cat > "__init__.py" << 'EOF'
"""IGAS - Integrated Automation & Scraping Tools"""
__version__ = "1.0.0"
__author__ = "sekretariatferadmi-byte"
EOF
print_success "Created __init__.py"

# Create main.py template
cat > "main.py" << 'EOF'
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IGAS Main Entry Point
"""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from shared.config import load_config
from shared.utils import setup_logging

def main():
    """Main entry point"""
    config = load_config()
    logger = setup_logging(config)
    
    logger.info("IGAS Started")
    print("""
    ╔═══════════════════════════════════════╗
    ║          🚀 IGAS v1.0.0 🚀            ║
    ║  Integrated Automation & Scraping    ║
    ╚═══════════════════════════════════════╝
    
    Available Tools:
    1. Instagram Tools
    2. Termux Bot
    3. Web Application
    4. CLI Tools
    5. Web Scrapers
    
    Run: python3 -m [module_name]
    """)

if __name__ == "__main__":
    main()
EOF
chmod +x main.py
print_success "Created main.py"

# Step 10: Create Basic Modules
print_header "Step 10: Creating Basic Module Templates"

# shared/config.py
cat > "shared/config.py" << 'EOF'
"""Configuration management"""
import os
from pathlib import Path
from dotenv import load_dotenv
import yaml

class Config:
    """Main configuration class"""
    
    def __init__(self):
        self.load_env()
        self.load_settings()
    
    def load_env(self):
        """Load .env file"""
        dotenv_path = Path(__file__).parent.parent / ".env"
        load_dotenv(dotenv_path)
    
    def load_settings(self):
        """Load YAML settings"""
        settings_path = Path(__file__).parent.parent / "config" / "settings.yaml"
        try:
            with open(settings_path, 'r') as f:
                self.settings = yaml.safe_load(f) or {}
        except FileNotFoundError:
            self.settings = {}
    
    def get(self, key, default=None):
        """Get environment variable or setting"""
        return os.getenv(key, default)

def load_config():
    """Factory function to load config"""
    return Config()
EOF
print_success "Created shared/config.py"

# shared/utils.py
cat > "shared/utils.py" << 'EOF'
"""Utility functions"""
import logging
from pathlib import Path
from loguru import logger

def setup_logging(config):
    """Setup logging configuration"""
    log_level = config.get("LOG_LEVEL", "INFO")
    log_file = config.get("LOG_FILE", "logs/igas.log")
    
    # Create logs directory if not exists
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    
    # Configure loguru
    logger.add(log_file, level=log_level)
    logger.add(lambda msg: print(msg, end=""), level=log_level)
    
    return logger

def ensure_dir(path):
    """Ensure directory exists"""
    Path(path).mkdir(parents=True, exist_ok=True)
    return Path(path)

def ensure_file(path, content=""):
    """Ensure file exists"""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content)
    return path
EOF
print_success "Created shared/utils.py"

# Step 11: Permissions
print_header "Step 11: Setting Permissions"
chmod -R 755 . 2>/dev/null || true
print_success "Permissions set"

# Step 12: Final Setup
print_header "Installation Complete! ✓"

echo -e "\n${GREEN}════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ IGAS Installation Successful!${NC}"
echo -e "${GREEN}════════════════════════════════════════${NC}\n"

echo "Next steps:"
echo "1. Edit configuration:"
echo -e "   ${BLUE}nano .env${NC}"
echo ""
echo "2. Run main program:"
echo -e "   ${BLUE}python3 main.py${NC}"
echo ""
echo "3. Start using tools:"
echo -e "   ${BLUE}python3 -m instagram_tools.auto_poster${NC}"
echo -e "   ${BLUE}python3 -m termux_bot.system_monitor${NC}"
echo -e "   ${BLUE}python3 -m cli_tools.file_manager${NC}"
echo ""
echo "Documentation: docs/INSTALLATION.md"
echo -e "\n${YELLOW}Make sure to configure .env file with your credentials!${NC}\n"

print_success "Installation finished!"
