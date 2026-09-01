# 🔥 IGAS API Reference

Dokumentasi lengkap API dan modul IGAS.

## Table of Contents

1. [Instagram Tools](#instagram-tools)
2. [Termux Bot](#termux-bot)
3. [CLI Tools](#cli-tools)
4. [Scrapers](#scrapers)
5. [Shared Modules](#shared-modules)

---

## Instagram Tools

### AutoPoster

Automatis posting ke Instagram.

```python
from instagram_tools import AutoPoster

# Initialize
poster = AutoPoster(username="user", password="pass")

# Login
if poster.login():
    # Post photo
    poster.post_photo(
        photo_path="/path/to/photo.jpg",
        caption="Hello Instagram! #test",
        location="Jakarta, Indonesia"
    )
    
    # Post carousel
    poster.post_carousel(
        media_paths=["photo1.jpg", "photo2.jpg"],
        caption="Multiple photos"
    )
    
    # Post story
    poster.post_story("/path/to/story.jpg")
    
    # Like and follow
    poster.like_post(media_id="123456")
    poster.follow_user(user_id="789012")
    
    # Logout
    poster.logout()
```

### InstagramBot

Bot untuk automation dan engagement.

```python
from instagram_tools import InstagramBot

# Initialize
bot = InstagramBot(username="user", password="pass")

# Login
if bot.login():
    # Auto like hashtag
    bot.auto_like_hashtag(
        hashtag="python",
        amount=10,
        delay=(2, 5)  # 2-5 seconds between likes
    )
    
    # Auto follow from hashtag
    bot.auto_follow_hashtag(
        hashtag="python",
        amount=5,
        delay=(3, 8)
    )
    
    # Auto unfollow non-followers
    bot.auto_unfollow_non_followers(delay=(2, 5))
    
    # Get stats
    stats = bot.get_stats()
    print(f"Likes: {stats['likes']}")
    print(f"Follows: {stats['follows']}")
    
    # Reset stats
    bot.reset_stats()
    
    # Logout
    bot.logout()
```

### Reporter

Report inappropriate content.

```python
from instagram_tools import Reporter

reporter = Reporter()

# Get available reasons
reasons = reporter.get_report_reasons()
# {1: "It's spam", 2: "It's abusive or harmful", ...}

# Report post
report = reporter.report_post(
    media_id="123456",
    reason_id=1,  # "It's spam"
    reason_text="Spam content"
)

# Report user
report = reporter.report_user(
    user_id="789012",
    reason_id=2,  # "It's abusive"
    reason_text="Harassment"
)

# Report comment
report = reporter.report_comment(
    comment_id="456789",
    reason_id=3,
    reason_text="Harmful content"
)

# Get all reports
all_reports = reporter.get_reports()

# Save to file
reporter.save_reports("reports.json")

# Clear reports
reporter.clear_reports()
```

---

## Termux Bot

### SystemMonitor

Monitor sistem resources.

```python
from termux_bot import SystemMonitor

monitor = SystemMonitor()

# Get CPU info
cpu = monitor.get_cpu_info()
print(f"CPU: {cpu['cpu_percent']}%")

# Get memory info
mem = monitor.get_memory_info()
print(f"Memory: {mem['percent']}%")

# Get disk info
disk = monitor.get_disk_info("/")
print(f"Disk: {disk['percent']}%")

# Get network info
net = monitor.get_network_info()
print(f"Sent: {net['bytes_sent']} bytes")

# Get top processes
processes = monitor.get_process_info()
for proc in processes[:5]:
    print(f"{proc['name']}: {proc['memory_percent']}%")

# Get full report
report = monitor.get_full_report()

# Print formatted stats
monitor.print_stats()
```

---

## CLI Tools

### FileManager

Manage files dari terminal.

```python
from cli_tools import FileManager

fm = FileManager()

# List files
files = fm.list_files(".", show_hidden=False)
for f in files:
    print(f"{f['name']} ({f['type']})")

# Copy file
fm.copy_file("source.txt", "destination.txt")

# Move file
fm.move_file("old_path.txt", "new_path.txt")

# Delete file
fm.delete_file("file.txt", confirm=True)

# Create directory
fm.create_directory("/path/to/new/dir")

# Get file info
info = fm.get_file_info("file.txt")
print(f"Size: {info['size_mb']:.2f}MB")
print(f"Path: {info['path']}")
```

**CLI Usage:**

```bash
# List files
python3 -m cli_tools.file_manager ls /path

# List with hidden files
python3 -m cli_tools.file_manager ls -h /path
```

---

## Scrapers

### InstagramScraper

Scrape Instagram public data (respect ToS).

```python
from scrapers import InstagramScraper

scraper = InstagramScraper(timeout=10)

# Search hashtag
results = scraper.search_hashtag(
    hashtag="python",
    limit=50
)

# Search user
user = scraper.search_user(username="username")
print(f"User found: {user['found']}")

# Get all results
all_results = scraper.get_results()

# Save results
scraper.save_results("scrape_results.json")

# Clear results
scraper.clear_results()
```

---

## Shared Modules

### Config

Manage configuration.

```python
from shared.config import load_config

# Load config
config = load_config()

# Get value
username = config.get("INSTAGRAM_USERNAME")
password = config.get("INSTAGRAM_PASSWORD")

# Get with default
api_key = config.get("API_KEY", "default_key")
```

### Utils

Utility functions.

```python
from shared.utils import setup_logging, ensure_dir, ensure_file, format_bytes

# Setup logging
logger = setup_logging(log_level="INFO", log_file="logs/app.log")

# Ensure directory exists
path = ensure_dir("data/results")

# Ensure file exists
file_path = ensure_file("config/settings.json", content="{}")

# Format bytes
size_str = format_bytes(1024 * 1024 * 10)  # "10.00 MB"
```

---

## Error Handling

```python
try:
    poster = AutoPoster("user", "pass")
    poster.login()
    poster.post_photo("photo.jpg", "Caption")
except Exception as e:
    print(f"Error: {e}")
finally:
    poster.logout()
```

---

## Best Practices

1. **Always use delays** antara requests
2. **Respect ToS** - Jangan spam atau harassment
3. **Use proxies** untuk menghindari ban
4. **Monitor logs** untuk debugging
5. **Handle exceptions** dengan baik
6. **Keep credentials safe** - Jangan commit .env

---

**For more help, check the source code or open an issue!**
