#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Bot
Automated bot for interactions and engagement
"""

import time
import random
from loguru import logger

try:
    from instagrapi import Client
except ImportError:
    Client = None


class InstagramBot:
    """Instagram Bot untuk automation dan engagement"""

    def __init__(self, username: str, password: str):
        """Initialize bot
        
        Args:
            username: Instagram username
            password: Instagram password
        """
        self.username = username
        self.password = password
        self.client = None
        self.is_active = False
        self.stats = {
            "likes": 0,
            "follows": 0,
            "comments": 0,
            "unfollows": 0
        }
    
    def login(self) -> bool:
        """Login to Instagram
        
        Returns:
            bool: Login status
        """
        if not Client:
            logger.error("instagrapi not installed")
            return False
        
        try:
            self.client = Client()
            self.client.login(self.username, self.password)
            self.is_active = True
            logger.info(f"✓ Bot logged in as {self.username}")
            return True
        except Exception as e:
            logger.error(f"✗ Bot login failed: {e}")
            return False
    
    def auto_like_hashtag(self, hashtag: str, amount: int = 10, delay: tuple = (2, 5)):
        """Auto like posts from hashtag
        
        Args:
            hashtag: Hashtag to like (without #)
            amount: Number of posts to like
            delay: Delay range between likes (min, max)
        """
        if not self.is_active:
            logger.error("Bot not active")
            return
        
        try:
            logger.info(f"Starting auto-like for #{hashtag}...")
            medias = self.client.hashtag_medias_recent(hashtag, amount=amount)
            
            for media in medias:
                try:
                    self.client.media_like(media.id)
                    self.stats["likes"] += 1
                    wait_time = random.uniform(delay[0], delay[1])
                    logger.debug(f"Liked post {media.id}, waiting {wait_time:.1f}s")
                    time.sleep(wait_time)
                except Exception as e:
                    logger.error(f"Like failed: {e}")
            
            logger.success(f"✓ Auto-like completed. Total: {self.stats['likes']}")
        except Exception as e:
            logger.error(f"Auto-like error: {e}")
    
    def auto_follow_hashtag(self, hashtag: str, amount: int = 5, delay: tuple = (3, 8)):
        """Auto follow users from hashtag
        
        Args:
            hashtag: Hashtag to search
            amount: Number of users to follow
            delay: Delay range between follows
        """
        if not self.is_active:
            logger.error("Bot not active")
            return
        
        try:
            logger.info(f"Starting auto-follow for #{hashtag}...")
            medias = self.client.hashtag_medias_recent(hashtag, amount=amount)
            
            for media in medias:
                try:
                    self.client.user_follow(media.user.pk)
                    self.stats["follows"] += 1
                    wait_time = random.uniform(delay[0], delay[1])
                    logger.debug(f"Followed {media.user.username}, waiting {wait_time:.1f}s")
                    time.sleep(wait_time)
                except Exception as e:
                    logger.error(f"Follow failed: {e}")
            
            logger.success(f"✓ Auto-follow completed. Total: {self.stats['follows']}")
        except Exception as e:
            logger.error(f"Auto-follow error: {e}")
    
    def auto_unfollow_non_followers(self, delay: tuple = (2, 5)):
        """Auto unfollow users who don't follow back
        
        Args:
            delay: Delay range between unfollows
        """
        if not self.is_active:
            logger.error("Bot not active")
            return
        
        try:
            logger.info("Checking non-followers...")
            user = self.client.account_info()
            following = self.client.user_following(user.pk)
            followers = self.client.user_followers(user.pk)
            
            followers_ids = [follower.pk for follower in followers]
            non_followers = [user for user in following if user.pk not in followers_ids]
            
            logger.info(f"Found {len(non_followers)} non-followers")
            
            for user in non_followers:
                try:
                    self.client.user_unfollow(user.pk)
                    self.stats["unfollows"] += 1
                    wait_time = random.uniform(delay[0], delay[1])
                    logger.debug(f"Unfollowed {user.username}")
                    time.sleep(wait_time)
                except Exception as e:
                    logger.error(f"Unfollow failed: {e}")
            
            logger.success(f"✓ Unfollow completed. Total: {self.stats['unfollows']}")
        except Exception as e:
            logger.error(f"Unfollow error: {e}")
    
    def get_stats(self) -> dict:
        """Get bot statistics
        
        Returns:
            dict: Current stats
        """
        return self.stats.copy()
    
    def reset_stats(self):
        """Reset statistics"""
        self.stats = {"likes": 0, "follows": 0, "comments": 0, "unfollows": 0}
        logger.info("Stats reset")
    
    def logout(self) -> bool:
        """Logout bot
        
        Returns:
            bool: Success status
        """
        try:
            if self.client:
                self.client.logout()
            self.is_active = False
            logger.info("✓ Bot logged out")
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
        logger.error("Missing Instagram credentials in .env")
        return
    
    bot = InstagramBot(username, password)
    
    if bot.login():
        logger.info("Bot ready for automation")
        # Example: bot.auto_like_hashtag("python", amount=5)
    else:
        logger.error("Failed to start bot")


if __name__ == "__main__":
    main()
