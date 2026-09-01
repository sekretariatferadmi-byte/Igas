# 🚨 IGAS Troubleshooting Guide

Solusi untuk error dan masalah yang umum terjadi.

## Common Issues & Solutions

### 1. Login Failed

**Error:** `LoginError: invalid username or password`

**Solutions:**
- Pastikan username dan password benar
- Coba login manual ke Instagram terlebih dahulu
- Jika 2FA enabled, disable temporarily atau gunakan app password
- Check apakah akun di-block

```bash
# Test login
python3 -c "
from instagram_tools import AutoPoster
poster = AutoPoster('username', 'password')
if poster.login():
    print('Login berhasil!')
else:
    print('Login gagal!')
"
```

---

### 2. Instagram Rate Limit

**Error:** `ConnectionError: Instagram limit reached`

**Solutions:**
- Tambah delay antara requests
- Gunakan proxy yang berbeda
- Tunggu beberapa jam sebelum mencoba lagi

```python
# Increase delay
bot.auto_like_hashtag(
    hashtag="python",
    amount=5,
    delay=(10, 15)  # 10-15 seconds
)
```

---

### 3. Module Not Found

**Error:** `ModuleNotFoundError: No module named 'instagrapi'`

**Solutions:**
```bash
# Reinstall specific module
pip3 install instagrapi --upgrade

# Reinstall all
pip3 install -r requirements.txt --force-reinstall

# Check installation
python3 -c "import instagrapi; print('OK')"
```

---

### 4. SSL Certificate Error

**Error:** `SSL: CERTIFICATE_VERIFY_FAILED`

**Solutions:**
```bash
# Update certificates
pip3 install --upgrade certifi

# Or disable SSL verify (not recommended)
# In code: verify_ssl=False
```

---

### 5. Database Lock

**Error:** `database is locked`

**Solutions:**
```bash
# Close all other processes using the database
pkill -f igas

# Remove lock file
rm -f data/.db-lock

# Restart application
python3 main.py
```

---

### 6. Permission Denied (Termux)

**Error:** `Permission denied`

**Solutions:**
```bash
# Give execute permission
chmod +x install.sh
chmod +x main.py

# Run with correct path
bash install.sh

# Or use python3 explicitly
python3 main.py
```

---

### 7. Proxy Not Working

**Error:** `ProxyError: proxy not responding`

**Solutions:**
```bash
# Test proxy
curl -x http://proxy:port http://google.com

# Edit .env
USE_PROXY=false  # Disable if problematic

# Or use different proxy
PROXY_LIST=new_proxies.txt
```

---

### 8. Timeout Issues

**Error:** `TimeoutError: connection timed out`

**Solutions:**
```python
# Increase timeout
config = {
    "timeout": 60,  # 60 seconds
    "retry_attempts": 5
}

poster = AutoPoster("user", "pass", config)
```

---

### 9. Memory Error

**Error:** `MemoryError: unable to allocate memory`

**Solutions:**
```bash
# Check available memory
free -h

# Limit worker threads
export ASYNC_WORKERS=2

# Clear cache
rm -rf cache/*
rm -rf __pycache__
```

---

### 10. Account Banned

**Error:** Account doesn't respond or blocked

**Solutions:**
- Stop using automation tools
- Wait 24-48 hours
- Check Instagram's help center
- Use VPN for different IP
- Create new test account

---

## Debugging Tips

### Enable Debug Logging

```bash
# Edit .env
LOG_LEVEL=DEBUG

# Or in code
from shared.utils import setup_logging
logger = setup_logging(log_level="DEBUG")
```

### Check Logs

```bash
# View logs
cat logs/igas.log

# Real-time logs
tail -f logs/igas.log

# Search for errors
grep "ERROR" logs/igas.log
```

### Test Individual Components

```python
# Test Instagram connection
from instagram_tools import AutoPoster
poster = AutoPoster("user", "pass")
print(poster.login())

# Test system monitor
from termux_bot import SystemMonitor
monitor = SystemMonitor()
monitor.print_stats()

# Test config
from shared.config import load_config
config = load_config()
print(config.get("INSTAGRAM_USERNAME"))
```

---

## Getting Help

1. **Check logs:** `cat logs/igas.log`
2. **Check docs:** `docs/` folder
3. **Search issues:** https://github.com/sekretariatferadmi-byte/Igas/issues
4. **Open new issue** dengan details:
   - Error message
   - Traceback
   - Python version
   - OS
   - Steps to reproduce

---

## Performance Optimization

```bash
# Use async operations
ASYNC_ENABLED=true
ASYNC_WORKERS=4

# Enable caching
CACHE_ENABLED=true
CACHE_TTL=3600

# Connection pooling
CONNECTION_POOL_SIZE=20
```

---

**Still having issues? Open an issue on GitHub!**
