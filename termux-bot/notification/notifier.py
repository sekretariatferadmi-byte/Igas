#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Notification System
Send notifications dan alerts
"""

from datetime import datetime
from loguru import logger
from typing import List, Dict, Any
import os


class Notifier:
    """Send various types of notifications"""

    def __init__(self):
        """Initialize notifier"""
        self.notifications = []
        self.is_termux = os.path.exists("/data/data/com.termux")
    
    def send_termux_notification(self, title: str, message: str) -> bool:
        """Send Termux notification
        
        Args:
            title: Notification title
            message: Notification message
            
        Returns:
            bool: Success status
        """
        if not self.is_termux:
            logger.warning("Not in Termux environment")
            return False
        
        try:
            os.system(f'termux-notification --title "{title}" --content "{message}"')
            self._store_notification("termux", title, message)
            return True
        except Exception as e:
            logger.error(f"Termux notification failed: {e}")
            return False
    
    def send_email(self, recipient: str, subject: str, body: str) -> bool:
        """Send email notification
        
        Args:
            recipient: Email address
            subject: Email subject
            body: Email body
            
        Returns:
            bool: Success status
        """
        try:
            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            
            sender = os.getenv("MAIL_USERNAME")
            password = os.getenv("MAIL_PASSWORD")
            smtp_server = os.getenv("MAIL_SERVER", "smtp.gmail.com")
            smtp_port = int(os.getenv("MAIL_PORT", 587))
            
            if not sender or not password:
                logger.warning("Email credentials not set")
                return False
            
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender, password)
                server.send_message(msg)
            
            logger.success(f"✓ Email sent to {recipient}")
            self._store_notification("email", subject, body)
            return True
        except Exception as e:
            logger.error(f"Email notification failed: {e}")
            return False
    
    def send_webhook(self, url: str, data: Dict[str, Any]) -> bool:
        """Send webhook notification
        
        Args:
            url: Webhook URL
            data: Data to send
            
        Returns:
            bool: Success status
        """
        try:
            import requests
            response = requests.post(url, json=data, timeout=10)
            success = response.status_code == 200
            
            if success:
                logger.success(f"✓ Webhook sent to {url}")
            else:
                logger.error(f"Webhook failed: {response.status_code}")
            
            self._store_notification("webhook", "Webhook", str(data))
            return success
        except Exception as e:
            logger.error(f"Webhook notification failed: {e}")
            return False
    
    def send_log(self, message: str, level: str = "INFO") -> bool:
        """Log notification
        
        Args:
            message: Message to log
            level: Log level
            
        Returns:
            bool: Success status
        """
        try:
            if level == "ERROR":
                logger.error(message)
            elif level == "WARNING":
                logger.warning(message)
            elif level == "SUCCESS":
                logger.success(message)
            else:
                logger.info(message)
            
            self._store_notification("log", level, message)
            return True
        except Exception as e:
            logger.error(f"Log notification failed: {e}")
            return False
    
    def _store_notification(self, notif_type: str, title: str, message: str):
        """Store notification in memory
        
        Args:
            notif_type: Type of notification
            title: Notification title
            message: Notification message
        """
        self.notifications.append({
            "type": notif_type,
            "title": title,
            "message": message,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_notifications(self) -> List[Dict[str, Any]]:
        """Get all notifications
        
        Returns:
            list: All notifications
        """
        return self.notifications.copy()
    
    def clear_notifications(self):
        """Clear notifications from memory"""
        self.notifications = []
        logger.info("Notifications cleared")


def main():
    """Main entry point"""
    notifier = Notifier()
    
    # Send various notifications
    notifier.send_log("Application started", "INFO")
    notifier.send_termux_notification("IGAS", "Bot started successfully")


if __name__ == "__main__":
    main()
