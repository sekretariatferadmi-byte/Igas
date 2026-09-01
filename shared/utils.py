"""Utility Functions"""

import os
import sys
from pathlib import Path

try:
    from loguru import logger
except ImportError:
    logger = None


def setup_logging(log_level: str = "INFO", log_file: str = "logs/igas.log"):
    """Setup logging configuration
    
    Args:
        log_level: Logging level
        log_file: Log file path
        
    Returns:
        Logger instance
    """
    if not logger:
        return None
    
    # Create logs directory
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    
    # Remove default handler
    logger.remove()
    
    # Add file handler
    logger.add(
        log_file,
        level=log_level,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="100 MB"
    )
    
    # Add console handler
    logger.add(
        sys.stdout,
        level=log_level,
        format="<level>{message}</level>"
    )
    
    return logger


def ensure_dir(path: str) -> Path:
    """Ensure directory exists
    
    Args:
        path: Directory path
        
    Returns:
        Path object
    """
    path_obj = Path(path)
    path_obj.mkdir(parents=True, exist_ok=True)
    return path_obj


def ensure_file(path: str, content: str = "") -> Path:
    """Ensure file exists
    
    Args:
        path: File path
        content: Initial content
        
    Returns:
        Path object
    """
    path_obj = Path(path)
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    
    if not path_obj.exists():
        path_obj.write_text(content)
    
    return path_obj


def format_bytes(bytes_value: int, decimals: int = 2) -> str:
    """Format bytes to human readable
    
    Args:
        bytes_value: Bytes value
        decimals: Decimal places
        
    Returns:
        Formatted string
    """
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(bytes_value)
    
    for unit in units:
        if size < 1024.0:
            return f"{size:.{decimals}f} {unit}"
        size /= 1024.0
    
    return f"{size:.{decimals}f} PB"
