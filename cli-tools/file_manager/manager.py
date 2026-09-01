#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CLI File Manager
Manage files and directories dari terminal
"""

import os
import shutil
from pathlib import Path
from loguru import logger
import click


class FileManager:
    """File management utilities"""

    @staticmethod
    def list_files(path: str = ".", show_hidden: bool = False) -> list:
        """List files in directory
        
        Args:
            path: Directory path
            show_hidden: Show hidden files
            
        Returns:
            list: Files and directories
        """
        try:
            items = []
            for item in Path(path).iterdir():
                if item.name.startswith(".") and not show_hidden:
                    continue
                is_dir = item.is_dir()
                size = item.stat().st_size if not is_dir else 0
                items.append({
                    "name": item.name,
                    "type": "dir" if is_dir else "file",
                    "size": size,
                    "path": str(item)
                })
            return sorted(items, key=lambda x: (x['type'] != 'dir', x['name']))
        except Exception as e:
            logger.error(f"List error: {e}")
            return []
    
    @staticmethod
    def copy_file(source: str, destination: str) -> bool:
        """Copy file
        
        Args:
            source: Source file path
            destination: Destination path
            
        Returns:
            bool: Success status
        """
        try:
            shutil.copy2(source, destination)
            logger.success(f"✓ Copied {source} → {destination}")
            return True
        except Exception as e:
            logger.error(f"Copy failed: {e}")
            return False
    
    @staticmethod
    def move_file(source: str, destination: str) -> bool:
        """Move file
        
        Args:
            source: Source file path
            destination: Destination path
            
        Returns:
            bool: Success status
        """
        try:
            shutil.move(source, destination)
            logger.success(f"✓ Moved {source} → {destination}")
            return True
        except Exception as e:
            logger.error(f"Move failed: {e}")
            return False
    
    @staticmethod
    def delete_file(path: str, confirm: bool = True) -> bool:
        """Delete file
        
        Args:
            path: File path
            confirm: Ask for confirmation
            
        Returns:
            bool: Success status
        """
        try:
            if confirm:
                response = input(f"Delete {path}? (y/n): ")
                if response.lower() != "y":
                    return False
            
            Path(path).unlink()
            logger.success(f"✓ Deleted {path}")
            return True
        except Exception as e:
            logger.error(f"Delete failed: {e}")
            return False
    
    @staticmethod
    def create_directory(path: str) -> bool:
        """Create directory
        
        Args:
            path: Directory path
            
        Returns:
            bool: Success status
        """
        try:
            Path(path).mkdir(parents=True, exist_ok=True)
            logger.success(f"✓ Created directory {path}")
            return True
        except Exception as e:
            logger.error(f"Create directory failed: {e}")
            return False
    
    @staticmethod
    def get_file_info(path: str) -> dict:
        """Get file information
        
        Args:
            path: File path
            
        Returns:
            dict: File info
        """
        try:
            stat = Path(path).stat()
            return {
                "path": str(Path(path).absolute()),
                "size": stat.st_size,
                "size_mb": stat.st_size / (1024**2),
                "created": stat.st_ctime,
                "modified": stat.st_mtime,
                "is_file": Path(path).is_file(),
                "is_dir": Path(path).is_dir()
            }
        except Exception as e:
            logger.error(f"File info error: {e}")
            return {}


@click.group()
def cli():
    """IGAS CLI File Manager"""
    pass


@cli.command()
@click.option('-h', '--hidden', is_flag=True, help='Show hidden files')
@click.argument('path', default='.')
def ls(hidden, path):
    """List files in directory"""
    fm = FileManager()
    files = fm.list_files(path, show_hidden=hidden)
    
    if not files:
        click.echo("Directory empty or not found")
        return
    
    click.echo(f"\n{'Name':<30} {'Type':<10} {'Size':<15}")
    click.echo("-" * 55)
    
    for item in files:
        size_str = f"{item['size'] / (1024**2):.2f}MB" if item['type'] == 'file' else "-"
        click.echo(f"{item['name']:<30} {item['type']:<10} {size_str:<15}")
    
    click.echo()


def main():
    """Main entry point"""
    cli()


if __name__ == "__main__":
    main()
