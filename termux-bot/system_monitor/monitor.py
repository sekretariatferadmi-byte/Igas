#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
System Monitor untuk Termux
Monitor sistem resources dan status
"""

import os
import psutil
import time
from datetime import datetime
from loguru import logger
from typing import Dict, Any


class SystemMonitor:
    """Monitor sistem resources"""

    def __init__(self):
        """Initialize monitor"""
        self.start_time = datetime.now()
        self.metrics = []
    
    def get_cpu_info(self) -> Dict[str, Any]:
        """Get CPU information
        
        Returns:
            dict: CPU stats
        """
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            cpu_count = psutil.cpu_count()
            
            return {
                "timestamp": datetime.now().isoformat(),
                "cpu_percent": cpu_percent,
                "cpu_count": cpu_count,
                "cpu_freq": psutil.cpu_freq().current if psutil.cpu_freq() else None
            }
        except Exception as e:
            logger.error(f"CPU info error: {e}")
            return {}
    
    def get_memory_info(self) -> Dict[str, Any]:
        """Get memory information
        
        Returns:
            dict: Memory stats
        """
        try:
            memory = psutil.virtual_memory()
            return {
                "timestamp": datetime.now().isoformat(),
                "total": memory.total,
                "available": memory.available,
                "used": memory.used,
                "percent": memory.percent
            }
        except Exception as e:
            logger.error(f"Memory info error: {e}")
            return {}
    
    def get_disk_info(self, path: str = "/") -> Dict[str, Any]:
        """Get disk information
        
        Args:
            path: Disk path
            
        Returns:
            dict: Disk stats
        """
        try:
            disk = psutil.disk_usage(path)
            return {
                "timestamp": datetime.now().isoformat(),
                "total": disk.total,
                "used": disk.used,
                "free": disk.free,
                "percent": disk.percent
            }
        except Exception as e:
            logger.error(f"Disk info error: {e}")
            return {}
    
    def get_network_info(self) -> Dict[str, Any]:
        """Get network information
        
        Returns:
            dict: Network stats
        """
        try:
            net = psutil.net_io_counters()
            return {
                "timestamp": datetime.now().isoformat(),
                "bytes_sent": net.bytes_sent,
                "bytes_recv": net.bytes_recv,
                "packets_sent": net.packets_sent,
                "packets_recv": net.packets_recv
            }
        except Exception as e:
            logger.error(f"Network info error: {e}")
            return {}
    
    def get_process_info(self, process_name: str = None) -> list:
        """Get process information
        
        Args:
            process_name: Filter by process name
            
        Returns:
            list: Process list
        """
        try:
            processes = []
            for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'cpu_percent']):
                if process_name and process_name.lower() not in proc.info['name'].lower():
                    continue
                processes.append({
                    "pid": proc.info['pid'],
                    "name": proc.info['name'],
                    "memory_percent": proc.info['memory_percent'],
                    "cpu_percent": proc.info['cpu_percent']
                })
            
            return sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:10]
        except Exception as e:
            logger.error(f"Process info error: {e}")
            return []
    
    def get_full_report(self) -> Dict[str, Any]:
        """Get complete system report
        
        Returns:
            dict: Full system stats
        """
        return {
            "timestamp": datetime.now().isoformat(),
            "uptime": (datetime.now() - self.start_time).total_seconds(),
            "cpu": self.get_cpu_info(),
            "memory": self.get_memory_info(),
            "disk": self.get_disk_info(),
            "network": self.get_network_info(),
            "processes_top": self.get_process_info()
        }
    
    def print_stats(self):
        """Print formatted stats to console"""
        report = self.get_full_report()
        
        print("\n" + "="*50)
        print("📊 SYSTEM MONITOR REPORT")
        print("="*50)
        
        if report['cpu']:
            print(f"\n🔧 CPU: {report['cpu']['cpu_percent']}%")
            print(f"   Cores: {report['cpu']['cpu_count']}")
        
        if report['memory']:
            mem = report['memory']
            print(f"\n💾 MEMORY: {mem['percent']}%")
            print(f"   Used: {mem['used'] / (1024**3):.2f}GB / {mem['total'] / (1024**3):.2f}GB")
        
        if report['disk']:
            disk = report['disk']
            print(f"\n💿 DISK: {disk['percent']}%")
            print(f"   Used: {disk['used'] / (1024**3):.2f}GB / {disk['total'] / (1024**3):.2f}GB")
        
        print("\n" + "="*50 + "\n")


def main():
    """Main entry point"""
    monitor = SystemMonitor()
    
    logger.info("System Monitor Started")
    
    try:
        while True:
            monitor.print_stats()
            time.sleep(10)  # Update every 10 seconds
    except KeyboardInterrupt:
        logger.info("Monitor stopped")


if __name__ == "__main__":
    main()
