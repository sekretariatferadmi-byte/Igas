#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IGAS Setup Configuration
For pip installation: pip install -e .
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="igas",
    version="1.0.0",
    author="sekretariatferadmi-byte",
    author_email="your_email@example.com",
    description="Integrated Automation & Scraping Tools - Instagram, Bot, Web Scraper, CLI Tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sekretariatferadmi-byte/Igas",
    project_urls={
        "Bug Tracker": "https://github.com/sekretariatferadmi-byte/Igas/issues",
        "Documentation": "https://github.com/sekretariatferadmi-byte/Igas/tree/main/docs",
        "Source Code": "https://github.com/sekretariatferadmi-byte/Igas",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "aiohttp>=3.8.0",
        "python-dotenv>=0.20.0",
        "pydantic>=1.9.0",
        "colorama>=0.4.6",
        "instagrapi>=2.0.0",
        "beautifulsoup4>=4.11.0",
        "selenium>=4.0.0",
        "flask>=2.2.0",
        "fastapi>=0.95.0",
        "uvicorn>=0.20.0",
        "sqlalchemy>=1.4.0",
        "loguru>=0.7.0",
        "pyyaml>=6.0",
        "click>=8.1.0",
        "tqdm>=4.65.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.3.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "pylint>=2.17.0",
        ],
        "docs": [
            "sphinx>=6.0.0",
            "sphinx-rtd-theme>=1.2.0",
        ],
        "scraping": [
            "playwright>=1.30.0",
            "scrapy>=2.8.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "igas=main:main",
            "igas-ig=instagram_tools.auto_poster:main",
            "igas-bot=termux_bot.system_monitor:main",
            "igas-cli=cli_tools.file_manager:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
