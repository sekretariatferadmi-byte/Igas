"""
Shared modules and utilities for IGAS
"""

__version__ = "1.0.0"
__author__ = "sekretariatferadmi-byte"

from .config import load_config
from .utils import setup_logging, ensure_dir, ensure_file

__all__ = [
    "load_config",
    "setup_logging",
    "ensure_dir",
    "ensure_file",
]
