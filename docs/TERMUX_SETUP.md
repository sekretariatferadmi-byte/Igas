# 📱 Setup IGAS di Termux

Panduan lengkap untuk menginstall dan menggunakan IGAS di Termux.

## 📋 Prasyarat

- **Termux** versi terbaru (dari F-Droid, bukan Play Store)
- **RAM** minimal 512MB
- **Storage** minimal 500MB
- **Internet** koneksi stabil

## 🚀 Instalasi Cepat

### 1. Buka Termux

Buka aplikasi Termux yang sudah diinstall.

### 2. Update System

```bash
pkg update -y
pkg upgrade -y
```

### 3. Install Dependencies

```bash
pkg install python3 python3-pip git curl wget -y
pkg install libffi-dev libssl-dev build-essential -y
```

### 4. Clone Repository

```bash
cd storage/downloads  # atau direktori lain
git clone https://github.com/sekretariatferadmi-byte/Igas.git
cd Igas
```

### 5. Run Installation Script

```bash
bash install.sh
```

Atau manual:

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

### 6. Konfigurasi

```bash
# Copy environment template
cp config/.env.example .env

# Edit dengan nano
nano .env
```

Isi dengan data Instagram dan settings Anda.

### 7. Test Installation

```bash
python3 main.py
```

Jika berhasil, akan menampilkan menu IGAS.

---

## ⚙️ Konfigurasi Lanjutan

### Mengaktifkan Storage Access

Untuk mengakses file di folder storage:

```bash
# Give Termux permission ke storage
termux-setup-storage
```

Akan diminta izin akses - pilih "Allow".

### Setup Task Scheduling (Cron)

Untuk menjalankan bot secara otomatis:

```bash
# Install cronie
pkg install cronie -y

# Start crond service
crond -b

# Edit crontab
crontab -e
```

Contoh schedule (jalankan setiap jam 9 pagi):

```crontab
0 9 * * * cd ~/Igas && python3 -m instagram_tools.auto_poster
```

### Menggunakan Waktu Sistem

```bash
# Set timezone
echo "Asia/Jakarta" > /etc/timezone
```

---

## 🔧 Troubleshooting Termux

### Error: "fatal: could not create work tree dir"

**Penyebab**: Storage permission tidak diizinkan

**Solusi**:
```bash
termux-setup-storage
cd storage/downloads
```

### Error: "pip3 not found"

**Penyebab**: Python3-pip tidak terinstall

**Solusi**:
```bash
pkg install python3-pip -y
```

### Error: "SSL: CERTIFICATE_VERIFY_FAILED"

**Penyebab**: Certificate issue

**Solusi**:
```bash
pip3 install --upgrade certifi
```

Atau disable SSL (tidak recommended):
```bash
pip3 install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org
```

### Error: "ModuleNotFoundError"

**Penyebab**: Requirements tidak terinstall

**Solusi**:
```bash
# Pastikan di folder Igas
cd ~/Igas

# Reinstall
pip3 install -r requirements.txt --force-reinstall
```

### Bot Berhenti/Timeout

**Penyebab**: Internet terputus atau Instagram block

**Solusi**:
1. Gunakan proxy (edit .env: `USE_PROXY=true`)
2. Tambah delay di antara request
3. Gunakan VPN

### Keyboard Tidak Muncul

**Penyebab**: Input method issue

**Solusi**:
```bash
apt install termux-api -y
termux-input-show
```

---

## 💾 Backup & Restore

### Backup Configuration

```bash
# Backup .env
cp .env backup/.env.backup

# Backup database
cp data/igas.db backup/igas_$(date +%Y%m%d).db.backup
```

### Restore Configuration

```bash
cp backup/.env.backup .env
```

---

## 📦 Update IGAS

```bash
cd ~/Igas
git pull origin main
pip3 install -r requirements.txt --upgrade
```

---

## 🚫 Uninstall

```bash
cd ~/
rm -rf Igas
```

---

## 📊 Performance Tips

1. **Gunakan Virtual Environment**: Isolasi dependencies
2. **Monitor Resource**: `top` atau `free -h`
3. **Limit Workers**: Edit `.env`, set `ASYNC_WORKERS=2`
4. **Clear Cache**: `rm -rf cache/*`
5. **Rotate Logs**: Delete logs lama di `logs/`

---

## 🔐 Security Tips

1. **Jangan share .env** - Berisi credentials!
2. **Use .gitignore** - .env sudah di .gitignore
3. **VPN untuk API**: Gunakan VPN yang reliable
4. **Rotate Credentials**: Ganti password Instagram berkala
5. **Monitor Account**: Check activity log Instagram

---

## 📞 Getting Help

Jika ada error:

1. **Baca log**: `cat logs/igas.log`
2. **Check Internet**: `curl google.com`
3. **Test Python**: `python3 -c "import requests; print('OK')"`
4. **Report Issue**: https://github.com/sekretariatferadmi-byte/Igas/issues

---

**Selamat! IGAS sudah siap digunakan di Termux! 🎉**
