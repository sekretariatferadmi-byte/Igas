#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IGAS Configuration Module
"""

from shared.config import load_config
from shared.utils import setup_logging, ensure_dir

# Setup logging
ensure_dir("logs")
ensure_dir("data")
ensure_dir("cache")
ensure_dir("results")

# Load configuration
config = load_config()
logger = setup_logging(
    log_level=config.get("LOG_LEVEL", "INFO"),
    log_file=config.get("LOG_FILE", "logs/igas.log")
)

logger.info("IGAS Configuration loaded successfully")
