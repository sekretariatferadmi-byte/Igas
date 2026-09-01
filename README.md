# 🚀 IGAS - Integrated Automation & Scraping Tools

> Koleksi lengkap tools untuk **automation**, **web scraping**, **CLI**, dan **bot** yang bisa dijalankan di Termux maupun sistem Linux/Windows.

## 📦 Apa ini?

**IGAS** adalah project yang menggabungkan berbagai jenis automation tools dalam satu repository:
- ✅ **Instagram Automation** - Auto posting, bot, reporting
- ✅ **Termux Bot** - Automation di terminal
- ✅ **Web Application** - Backend + Frontend
- ✅ **CLI Tool** - Command-line utilities
- ✅ **Data Scraper** - Web scraping otomatis

---

## 📂 Struktur Folder

```
igas/
├── instagram-tools/          # Tools untuk Instagram
│   ├── auto_poster/          # Auto post ke Instagram
│   ├── bot/                  # Instagram Bot
│   └── reporter/             # Reporting tool
├── termux-bot/               # Bot untuk Termux
│   ├── system_monitor/       # Monitor sistem
│   ├── task_scheduler/       # Task automation
│   └── notification/         # Alert system
├── web-app/                  # Web Application
│   ├── backend/              # API/Backend (Python/Node)
│   ├── frontend/             # UI (React/Vue)
│   └── database/             # DB config
├── cli-tools/                # Command Line Tools
│   ├── file_manager/         # File operations
│   ├── data_converter/       # Format converter
│   └── batch_processor/      # Batch processing
├── scrapers/                 # Web Scrapers
│   ├── instagram_scraper/    # Instagram data scraper
│   ├── web_scraper/          # General web scraper
│   └── api_scraper/          # API data scraper
├── shared/                   # Library bersama
│   ├── config/               # Konfigurasi
│   ├── utils/                # Utility functions
│   └── modules/              # Shared modules
├── docs/                     # Dokumentasi
│   ├── INSTALLATION.md       # Panduan instalasi
│   ├── TERMUX_SETUP.md       # Setup Termux
│   └── API_REFERENCE.md      # API docs
├── config/                   # File konfigurasi
│   ├── .env.example          # Template env
���   └── settings.yaml         # Settings umum
├── requirements.txt          # Python dependencies
├── package.json              # Node dependencies (opsional)
├── setup.py                  # Python setup
├── install.sh                # Script instalasi
└── .gitignore                # Git ignore rules
```

---

## 🚀 Quick Start

### Opsi 1: Instalasi Cepat (Termux)
```bash
git clone https://github.com/sekretariatferadmi-byte/Igas.git
cd Igas
bash install.sh
```

### Opsi 2: Manual Setup
```bash
# Update sistem
pkg update -y

# Install dependencies
pkg install python3 git curl -y

# Clone repo
git clone https://github.com/sekretariatferadmi-byte/Igas.git
cd Igas

# Install Python requirements
pip3 install -r requirements.txt
```

---

## 🛠️ Tools yang Tersedia

### 📱 Instagram Tools
```bash
python3 -m instagram_tools.auto_poster
python3 -m instagram_tools.bot
python3 -m instagram_tools.reporter
```

### 🤖 Termux Bot
```bash
python3 -m termux_bot.system_monitor
python3 -m termux_bot.task_scheduler
python3 -m termux_bot.notification
```

### 🌐 Web Application
```bash
cd web-app/backend
python3 app.py
```

### 💻 CLI Tools
```bash
python3 -m cli_tools.file_manager
python3 -m cli_tools.data_converter
python3 -m cli_tools.batch_processor
```

### 🕷️ Web Scrapers
```bash
python3 -m scrapers.instagram_scraper
python3 -m scrapers.web_scraper
python3 -m scrapers.api_scraper
```

---

## ⚙️ Konfigurasi

Sebelum menggunakan tool, buat file `.env`:

```bash
cp config/.env.example .env
nano .env
```

Isi dengan data Anda:
```env
# Instagram
INSTAGRAM_USERNAME=your_username
INSTAGRAM_PASSWORD=your_password
INSTAGRAM_API_KEY=your_api_key

# Proxy (opsional)
USE_PROXY=false
PROXY_LIST=proxies.txt

# Database
DB_URL=sqlite:///data.db

# API Keys
API_KEY=your_api_key
SECRET_KEY=your_secret_key
```

---

## 📖 Dokumentasi Lengkap

- [Instalasi di Termux](docs/TERMUX_SETUP.md)
- [Panduan Instalasi Umum](docs/INSTALLATION.md)
- [API Reference](docs/API_REFERENCE.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

---

## 🔧 Requirements

### Sistem
- Python 3.8+
- Git
- RAM minimal 512MB

### Python Packages
- requests
- selenium / playwright (untuk web scraping)
- aiohttp (async requests)
- flask / fastapi (untuk web app)
- pydantic (data validation)
- python-dotenv (env management)

Lihat `requirements.txt` untuk daftar lengkap.

---

## ⚠️ Disclaimer

⚠️ **Tools ini untuk tujuan edukatif dan testing saja!**

Penggunaan untuk:
- ❌ Harassment, spam, atau cyberbullying
- ❌ Melanggar ToS platform apapun
- ❌ Aktivitas ilegal

Bisa berakhir dengan **banned akun** atau **tindakan legal**.

---

## 📝 Lisensi

GPL-3.0 License - Bebas digunakan, dimodifikasi, tapi harus open source.

---

## 🤝 Kontribusi

Pull request welcome! Untuk kontribusi besar:
1. Fork repository
2. Buat branch feature (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

---

## 📞 Support

- 🐛 Report bug di [Issues](https://github.com/sekretariatferadmi-byte/Igas/issues)
- 💬 Diskusi di [Discussions](https://github.com/sekretariatferadmi-byte/Igas/discussions)
- 📧 Email: [contact info]

---

## 🎯 Roadmap

- [ ] Instagram Auto Poster v1.0
- [ ] Termux System Monitor
- [ ] Web App Dashboard
- [ ] CLI Tool Suite
- [ ] Advanced Web Scraper
- [ ] Mobile App Support
- [ ] Docker Support

---

**⭐ Jika project ini membantu, jangan lupa beri star!**

Happy coding! 🚀
