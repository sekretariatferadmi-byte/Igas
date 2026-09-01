# 📱 Setup IGAS di Sistem Linux/Windows

Panduan instalasi lengkap untuk Linux dan Windows.

## 🐧 Linux Installation

### Prerequisites

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3 python3-pip python3-dev python3-venv -y
sudo apt install build-essential libssl-dev libffi-dev git -y
```

### Installation Steps

```bash
# Clone repository
git clone https://github.com/sekretariatferadmi-byte/Igas.git
cd Igas

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip3 install --upgrade pip
pip3 install -r requirements.txt

# Setup configuration
cp config/.env.example .env
nano .env  # Edit dengan credentials Anda
```

### Run IGAS

```bash
# Main program
python3 main.py

# Instagram Tools
python3 -m instagram_tools.auto_poster

# Termux Bot
python3 -m termux_bot.system_monitor

# CLI Tools
python3 -m cli_tools.file_manager

# Scrapers
python3 -m scrapers.instagram_scraper
```

---

## 🪟 Windows Installation

### Prerequisites

1. **Download Python 3.8+**
   - Go to https://www.python.org/downloads/
   - Download Python 3.11 or latest
   - **Important**: Check "Add Python to PATH"

2. **Download Git**
   - Go to https://git-scm.com/download/win
   - Install Git Bash

3. **Open Command Prompt or PowerShell**

### Installation Steps

```powershell
# Check Python installation
python --version

# Clone repository
git clone https://github.com/sekretariatferadmi-byte/Igas.git
cd Igas

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Setup configuration
copy config\.env.example .env
# Edit .env with your credentials (use Notepad)
```

### Run IGAS

```powershell
# Main program
python main.py

# Instagram Tools
python -m instagram_tools.auto_poster

# System Monitor
python -m termux_bot.system_monitor

# CLI Tools
python -m cli_tools.file_manager
```

---

## 🐳 Docker Installation (Optional)

### Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

### Build and Run

```bash
# Build image
docker build -t igas:latest .

# Run container
docker run -it -v $(pwd):/app igas:latest
```

---

## ✅ Verification

Setelah instalasi, verify dengan:

```bash
# Check all imports
python3 -c "from instagram_tools import *; from termux_bot import *; print('✓ All modules loaded')"

# Check configuration
python3 -c "from shared.config import load_config; config = load_config(); print('✓ Config loaded')"

# Run tests (if available)
pytest tests/ -v
```

---

## 🔧 Troubleshooting

### ImportError: No module named 'instagrapi'

```bash
pip3 install instagrapi --upgrade
```

### SSL Error

```bash
pip3 install --upgrade certifi
```

### Permission Denied (Linux)

```bash
chmod +x install.sh
bash install.sh
```

### ModuleNotFoundError

```bash
# Reinstall all requirements
pip3 install -r requirements.txt --force-reinstall
```

---

## 📚 Next Steps

1. Edit `.env` dengan credentials
2. Run `python3 main.py` untuk test
3. Baca dokumentasi modul yang ingin digunakan
4. Start using tools!

---

**Setup selesai! Happy coding! 🚀**
