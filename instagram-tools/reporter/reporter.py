#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Reporter
Report inappropriate content to Instagram
"""

import json
from datetime import datetime
from pathlib import Path
from loguru import logger


class Reporter:
    """Report inappropriate content"""

    # Report reasons
    REPORT_REASONS = {
        1: "It's spam",
        2: "It's abusive or harmful",
        3: "It expresses intentions of self-harm or suicide",
        4: "It sells or promotes illegal or regulated goods",
        5: "It violates intellectual property rights",
        6: "It's a scam or fraud",
        7: "It infringes on my privacy",
        8: "It's someone impersonating me"
    }

    def __init__(self, client=None):
        """Initialize reporter
        
        Args:
            client: Instagram client instance
        """
        self.client = client
        self.reports = []
    
    def report_post(self, media_id: str, reason_id: int, reason_text: str = "") -> dict:
        """Report a post
        
        Args:
            media_id: Post ID to report
            reason_id: Report reason ID
            reason_text: Additional reason details
            
        Returns:
            dict: Report details
        """
        if reason_id not in self.REPORT_REASONS:
            logger.error(f"Invalid reason ID: {reason_id}")
            return {}
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "type": "post",
            "media_id": media_id,
            "reason_id": reason_id,
            "reason": self.REPORT_REASONS[reason_id],
            "additional_info": reason_text,
            "status": "submitted"
        }
        
        self.reports.append(report)
        logger.info(f"✓ Reported post {media_id} for: {report['reason']}")
        return report
    
    def report_user(self, user_id: str, reason_id: int, reason_text: str = "") -> dict:
        """Report a user
        
        Args:
            user_id: User ID to report
            reason_id: Report reason ID
            reason_text: Additional details
            
        Returns:
            dict: Report details
        """
        if reason_id not in self.REPORT_REASONS:
            logger.error(f"Invalid reason ID: {reason_id}")
            return {}
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "type": "user",
            "user_id": user_id,
            "reason_id": reason_id,
            "reason": self.REPORT_REASONS[reason_id],
            "additional_info": reason_text,
            "status": "submitted"
        }
        
        self.reports.append(report)
        logger.info(f"✓ Reported user {user_id} for: {report['reason']}")
        return report
    
    def report_comment(self, comment_id: str, reason_id: int, reason_text: str = "") -> dict:
        """Report a comment
        
        Args:
            comment_id: Comment ID
            reason_id: Report reason ID
            reason_text: Additional details
            
        Returns:
            dict: Report details
        """
        if reason_id not in self.REPORT_REASONS:
            logger.error(f"Invalid reason ID: {reason_id}")
            return {}
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "type": "comment",
            "comment_id": comment_id,
            "reason_id": reason_id,
            "reason": self.REPORT_REASONS[reason_id],
            "additional_info": reason_text,
            "status": "submitted"
        }
        
        self.reports.append(report)
        logger.info(f"✓ Reported comment {comment_id}")
        return report
    
    def get_report_reasons(self) -> dict:
        """Get all available report reasons
        
        Returns:
            dict: Report reasons
        """
        return self.REPORT_REASONS.copy()
    
    def get_reports(self) -> list:
        """Get all reports
        
        Returns:
            list: List of reports
        """
        return self.reports.copy()
    
    def save_reports(self, filename: str = "reports.json"):
        """Save reports to file
        
        Args:
            filename: Output filename
        """
        try:
            Path("results").mkdir(exist_ok=True)
            filepath = Path("results") / filename
            
            with open(filepath, "w") as f:
                json.dump(self.reports, f, indent=2)
            
            logger.success(f"✓ Reports saved to {filepath}")
        except Exception as e:
            logger.error(f"Failed to save reports: {e}")
    
    def clear_reports(self):
        """Clear all reports from memory"""
        self.reports = []
        logger.info("Reports cleared")


def main():
    """Main entry point"""
    reporter = Reporter()
    
    logger.info("\nAvailable report reasons:")
    for reason_id, reason_text in reporter.get_report_reasons().items():
        print(f"{reason_id}. {reason_text}")


if __name__ == "__main__":
    main()
