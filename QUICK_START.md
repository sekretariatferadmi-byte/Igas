# IGAS - Integrated Automation & Scraping Tools

An all-in-one toolkit for automation, web scraping, and social media management.

## Quick Start

### Installation

```bash
git clone https://github.com/sekretariatferadmi-byte/Igas.git
cd Igas
bash install.sh
```

### Configuration

```bash
cp config/.env.example .env
nano .env  # Edit with your credentials
```

### Run

```bash
# Main program
python3 main.py

# Or individual tools
python3 -m instagram_tools.auto_poster
python3 -m termux_bot.system_monitor
python3 -m cli_tools.file_manager
```

## Features

✅ **Instagram Tools** - Auto posting, bot, reporting
✅ **Termux Bot** - System monitor, task scheduler, notifications
✅ **Web Application** - FastAPI backend with REST API
✅ **CLI Tools** - File manager and utilities
✅ **Web Scrapers** - Instagram and web scraping
✅ **Task Scheduler** - Automate recurring tasks
✅ **Notifications** - Email, webhook, Termux notifications

## Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Termux Setup](docs/TERMUX_SETUP.md)
- [API Reference](docs/API_REFERENCE.md)
- [Troubleshooting](docs/TROUBLESHOOTING.md)

## Project Structure

```
igas/
├── instagram-tools/     # Instagram automation
├── termux-bot/          # Termux utilities
├── web-app/             # Web application
├── cli-tools/           # Command-line tools
├── scrapers/            # Web scrapers
├── shared/              # Shared modules
├── docs/                # Documentation
├── config/              # Configuration files
├── logs/                # Application logs
├── data/                # Data storage
└── requirements.txt     # Python dependencies
```

## Requirements

- Python 3.8+
- pip (Python package manager)
- Git
- RAM: 512MB minimum
- Storage: 500MB minimum

## Support

- 📖 [Documentation](docs/)
- 🐛 [Report Issues](https://github.com/sekretariatferadmi-byte/Igas/issues)
- 💬 [Discussions](https://github.com/sekretariatferadmi-byte/Igas/discussions)

## License

GPL-3.0 License - See LICENSE file

## Disclaimer

⚠️ Use responsibly. Respect platform ToS and laws.

---

**Star this repo if it helps you! ⭐**
