"""Configuration Management"""

import os
from pathlib import Path
from dotenv import load_dotenv

try:
    import yaml
except ImportError:
    yaml = None


class Config:
    """Application configuration"""

    def __init__(self, env_path: str = ".env"):
        """Initialize config
        
        Args:
            env_path: Path to .env file
        """
        self.env_path = Path(env_path)
        self.settings = {}
        self.load_env()
        self.load_yaml()
    
    def load_env(self):
        """Load environment variables from .env"""
        if self.env_path.exists():
            load_dotenv(self.env_path)
    
    def load_yaml(self):
        """Load YAML settings"""
        if not yaml:
            return
        
        settings_path = Path("config/settings.yaml")
        if settings_path.exists():
            try:
                with open(settings_path, 'r', encoding='utf-8') as f:
                    self.settings = yaml.safe_load(f) or {}
            except Exception as e:
                print(f"Error loading YAML: {e}")
    
    def get(self, key: str, default=None):
        """Get config value
        
        Args:
            key: Config key
            default: Default value
            
        Returns:
            Config value or default
        """
        # Try environment first
        env_value = os.getenv(key)
        if env_value is not None:
            return env_value
        
        # Then try YAML
        if key in self.settings:
            return self.settings[key]
        
        return default


def load_config(env_path: str = ".env") -> Config:
    """Load configuration
    
    Args:
        env_path: Path to .env file
        
    Returns:
        Config object
    """
    return Config(env_path)
