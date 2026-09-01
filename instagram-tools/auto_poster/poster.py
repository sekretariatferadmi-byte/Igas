#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Auto Poster
Automatically post content to Instagram with scheduling
"""

import time
import os
from datetime import datetime
from pathlib import Path
from loguru import logger

try:
    from instagrapi import Client
except ImportError:
    logger.error("instagrapi not installed. Run: pip3 install instagrapi")
    Client = None


class AutoPoster:
    """Auto post ke Instagram"""

    def __init__(self, username: str, password: str, config: dict = None):
        """Initialize Instagram client
        
        Args:
            username: Instagram username
            password: Instagram password
            config: Configuration dictionary
        """
        self.username = username
        self.password = password
        self.config = config or {}
        self.client = None
        self.is_logged_in = False
        
    def login(self) -> bool:
        """Login to Instagram
        
        Returns:
            bool: True if login successful
        """
        if not Client:
            logger.error("instagrapi not installed")
            return False
            
        try:
            self.client = Client()
            self.client.login(self.username, self.password)
            self.is_logged_in = True
            logger.info(f"✓ Logged in as {self.username}")
            return True
        except Exception as e:
            logger.error(f"✗ Login failed: {e}")
            return False
    
    def post_photo(self, photo_path: str, caption: str = "", location: str = None) -> bool:
        """Post a photo to Instagram
        
        Args:
            photo_path: Path to photo file
            caption: Post caption
            location: Location tag
            
        Returns:
            bool: True if successful
        """
        if not self.is_logged_in:
            logger.error("Not logged in. Call login() first.")
            return False
        
        try:
            photo_path = Path(photo_path)
            if not photo_path.exists():
                logger.error(f"Photo not found: {photo_path}")
                return False
            
            logger.info(f"Posting photo: {photo_path}")
            media = self.client.photo_upload(
                photo_path,
                caption=caption,
                location=location
            )
            logger.success(f"✓ Posted successfully. ID: {media.id}")
            return True
        except Exception as e:
            logger.error(f"✗ Post failed: {e}")
            return False
    
    def post_carousel(self, media_paths: list, caption: str = "") -> bool:
        """Post carousel (multiple photos/videos)
        
        Args:
            media_paths: List of file paths
            caption: Post caption
            
        Returns:
            bool: True if successful
        """
        if not self.is_logged_in:
            logger.error("Not logged in")
            return False
        
        try:
            logger.info(f"Posting carousel with {len(media_paths)} items")
            media = self.client.album_upload(
                media_paths,
                caption=caption
            )
            logger.success(f"✓ Carousel posted. ID: {media.id}")
            return True
        except Exception as e:
            logger.error(f"✗ Carousel post failed: {e}")
            return False
    
    def post_story(self, media_path: str) -> bool:
        """Post to Instagram Story
        
        Args:
            media_path: Path to media file
            
        Returns:
            bool: True if successful
        """
        if not self.is_logged_in:
            logger.error("Not logged in")
            return False
        
        try:
            logger.info(f"Posting to story: {media_path}")
            self.client.photo_upload_to_story(media_path)
            logger.success("✓ Story posted successfully")
            return True
        except Exception as e:
            logger.error(f"✗ Story post failed: {e}")
            return False
    
    def like_post(self, media_id: str) -> bool:
        """Like a post
        
        Args:
            media_id: Media ID to like
            
        Returns:
            bool: True if successful
        """
        if not self.is_logged_in:
            return False
        
        try:
            self.client.media_like(media_id)
            logger.debug(f"Liked post: {media_id}")
            return True
        except Exception as e:
            logger.error(f"Like failed: {e}")
            return False
    
    def follow_user(self, user_id: str) -> bool:
        """Follow a user
        
        Args:
            user_id: User ID to follow
            
        Returns:
            bool: True if successful
        """
        if not self.is_logged_in:
            return False
        
        try:
            self.client.user_follow(user_id)
            logger.debug(f"Followed user: {user_id}")
            return True
        except Exception as e:
            logger.error(f"Follow failed: {e}")
            return False
    
    def logout(self) -> bool:
        """Logout from Instagram
        
        Returns:
            bool: True if successful
        """
        try:
            if self.client:
                self.client.logout()
            self.is_logged_in = False
            logger.info("✓ Logged out")
            return True
        except Exception as e:
            logger.error(f"Logout failed: {e}")
            return False


def main():
    """Main entry point"""
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")
    
    if not username or not password:
        logger.error("INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD not set in .env")
        return
    
    poster = AutoPoster(username, password)
    
    if poster.login():
        logger.info("Logged in successfully!")
        logger.info("Ready to post content.")
    else:
        logger.error("Failed to login")


if __name__ == "__main__":
    main()
