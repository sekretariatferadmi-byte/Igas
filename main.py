#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IGAS - Main Entry Point
Integrated Automation & Scraping Tools
"""

import sys
import os
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from shared.config import load_config
from shared.utils import setup_logging, ensure_dir
from loguru import logger


def print_banner():
    """Print application banner"""
    banner = """
    ╔════════════════════════════════════════╗
    ║                                        ║
    ║        🚀 IGAS v1.0.0 🚀              ║
    ║  Integrated Automation & Scraping     ║
    ║                                        ║
    ║  Instagram Tools • Bot • Scraper      ║
    ║  CLI Tools • Web App • Scheduler      ║
    ║                                        ║
    ╚═════════════════���══════════════════════╝
    """
    print(banner)


def print_menu():
    """Print main menu"""
    menu = """
    📋 MAIN MENU
    
    1. Instagram Tools
       └─ Auto Poster
       └─ Bot
       └─ Reporter
    
    2. Termux Bot
       └─ System Monitor
       └─ Task Scheduler
       └─ Notification
    
    3. Web Application
       └─ Start API Server
    
    4. CLI Tools
       └─ File Manager
    
    5. Web Scrapers
       └─ Instagram Scraper
    
    6. System Information
    
    0. Exit
    
    """
    print(menu)


def show_instagram_menu():
    """Instagram tools submenu"""
    print("""
    📱 INSTAGRAM TOOLS
    
    1. Auto Poster - Automatically post to Instagram
    2. Bot - Auto engagement (likes, follows)
    3. Reporter - Report inappropriate content
    
    0. Back to main menu
    """)


def show_bot_menu():
    """Bot tools submenu"""
    print("""
    🤖 TERMUX BOT
    
    1. System Monitor - Monitor CPU, RAM, Disk
    2. Task Scheduler - Schedule automated tasks
    3. Notification - Send notifications
    
    0. Back to main menu
    """)


def main_menu():
    """Main application loop"""
    config = load_config()
    setup_logging(
        log_level=config.get("LOG_LEVEL", "INFO"),
        log_file=config.get("LOG_FILE", "logs/igas.log")
    )
    
    logger.info("IGAS Application Started")
    
    while True:
        print_banner()
        print_menu()
        
        try:
            choice = input("Select option: ").strip()
            
            if choice == "1":
                instagram_submenu(config)
            elif choice == "2":
                bot_submenu(config)
            elif choice == "3":
                web_app_menu(config)
            elif choice == "4":
                cli_menu(config)
            elif choice == "5":
                scraper_menu(config)
            elif choice == "6":
                show_system_info()
            elif choice == "0":
                print("\n👋 Goodbye!\n")
                logger.info("IGAS Application Closed")
                break
            else:
                print("❌ Invalid option\n")
        except KeyboardInterrupt:
            print("\n\n⚠️  Application interrupted\n")
            logger.info("Application interrupted by user")
            break
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"❌ Error: {e}\n")


def instagram_submenu(config):
    """Instagram tools submenu"""
    while True:
        show_instagram_menu()
        choice = input("Select option: ").strip()
        
        if choice == "1":
            print("\n📝 Auto Poster")
            print("-" * 40)
            username = config.get("INSTAGRAM_USERNAME")
            if not username:
                print("❌ INSTAGRAM_USERNAME not set in .env")
            else:
                print(f"✓ Ready to post as @{username}")
                print("Use: python3 -m instagram_tools.auto_poster")
        
        elif choice == "2":
            print("\n🤖 Instagram Bot")
            print("-" * 40)
            username = config.get("INSTAGRAM_USERNAME")
            if not username:
                print("❌ INSTAGRAM_USERNAME not set in .env")
            else:
                print(f"✓ Bot ready for @{username}")
                print("Use: python3 -m instagram_tools.bot")
        
        elif choice == "3":
            print("\n📢 Reporter")
            print("-" * 40)
            print("Report inappropriate content to Instagram")
            print("Use: python3 -m instagram_tools.reporter")
        
        elif choice == "0":
            break
        else:
            print("❌ Invalid option\n")
        
        input("\nPress Enter to continue...")


def bot_submenu(config):
    """Bot tools submenu"""
    while True:
        show_bot_menu()
        choice = input("Select option: ").strip()
        
        if choice == "1":
            print("\n📊 System Monitor")
            print("-" * 40)
            try:
                from termux_bot.system_monitor import SystemMonitor
                monitor = SystemMonitor()
                monitor.print_stats()
            except Exception as e:
                logger.error(f"Monitor error: {e}")
                print(f"❌ Error: {e}")
        
        elif choice == "2":
            print("\n⏰ Task Scheduler")
            print("-" * 40)
            print("Schedule automated tasks")
            print("Use: python3 -m termux_bot.task_scheduler")
        
        elif choice == "3":
            print("\n🔔 Notification")
            print("-" * 40)
            print("Send notifications and alerts")
            print("Use: python3 -m termux_bot.notification")
        
        elif choice == "0":
            break
        else:
            print("❌ Invalid option\n")
        
        input("\nPress Enter to continue...")


def web_app_menu(config):
    """Web application menu"""
    print("\n🌐 Web Application")
    print("-" * 40)
    host = config.get("API_HOST", "0.0.0.0")
    port = config.get("API_PORT", "5000")
    print(f"API Server ready at http://{host}:{port}")
    print("\nStart with:")
    print(f"  python3 -m web_app.backend.app")
    print(f"\nAccess API docs at:")
    print(f"  http://localhost:{port}/docs")
    input("\nPress Enter to continue...")


def cli_menu(config):
    """CLI tools menu"""
    print("\n💻 CLI Tools")
    print("-" * 40)
    print("File Manager - Manage files and directories")
    print("\nUsage:")
    print("  python3 -m cli_tools.file_manager ls /path")
    print("  python3 -m cli_tools.file_manager cp source dest")
    input("\nPress Enter to continue...")


def scraper_menu(config):
    """Scraper menu"""
    print("\n🕷️  Web Scrapers")
    print("-" * 40)
    print("Instagram Scraper - Scrape Instagram public data")
    print("\nUsage:")
    print("  python3 -m scrapers.instagram_scraper")
    print("\n⚠️  Note: Only scrape public data. Respect ToS!")
    input("\nPress Enter to continue...")


def show_system_info():
    """Show system information"""
    print("\n📈 System Information")
    print("-" * 40)
    try:
        from termux_bot.system_monitor import SystemMonitor
        monitor = SystemMonitor()
        monitor.print_stats()
    except Exception as e:
        logger.error(f"Error: {e}")
        print(f"❌ Error: {e}")
    input("\nPress Enter to continue...")


if __name__ == "__main__":
    try:
        main_menu()
    except Exception as e:
        print(f"\n❌ Fatal Error: {e}")
        if logger:
            logger.critical(f"Fatal error: {e}")
        sys.exit(1)
