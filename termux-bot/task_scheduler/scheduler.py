#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Task Scheduler
Schedule dan automate tasks
"""

import schedule
import time
from datetime import datetime
from loguru import logger
from typing import Callable, Any


class TaskScheduler:
    """Schedule dan manage tasks"""

    def __init__(self):
        """Initialize scheduler"""
        self.tasks = {}
        self.is_running = False
    
    def add_job(
        self,
        job_name: str,
        func: Callable,
        interval: int,
        unit: str = "seconds",
        *args,
        **kwargs
    ):
        """Add a scheduled job
        
        Args:
            job_name: Unique job identifier
            func: Function to execute
            interval: Interval between executions
            unit: Time unit (seconds, minutes, hours, days)
            *args, **kwargs: Arguments for function
        """
        try:
            if unit == "seconds":
                job = schedule.every(interval).seconds.do(func, *args, **kwargs)
            elif unit == "minutes":
                job = schedule.every(interval).minutes.do(func, *args, **kwargs)
            elif unit == "hours":
                job = schedule.every(interval).hours.do(func, *args, **kwargs)
            elif unit == "days":
                job = schedule.every(interval).days.do(func, *args, **kwargs)
            else:
                logger.error(f"Invalid unit: {unit}")
                return False
            
            self.tasks[job_name] = {
                "job": job,
                "func": func,
                "interval": interval,
                "unit": unit,
                "created_at": datetime.now().isoformat(),
                "executions": 0,
                "last_run": None
            }
            
            logger.success(f"✓ Job '{job_name}' scheduled every {interval} {unit}")
            return True
        except Exception as e:
            logger.error(f"Failed to add job: {e}")
            return False
    
    def remove_job(self, job_name: str) -> bool:
        """Remove a scheduled job
        
        Args:
            job_name: Job identifier
            
        Returns:
            bool: Success status
        """
        if job_name in self.tasks:
            schedule.cancel_job(self.tasks[job_name]["job"])
            del self.tasks[job_name]
            logger.info(f"Job '{job_name}' removed")
            return True
        return False
    
    def get_jobs(self) -> dict:
        """Get all scheduled jobs
        
        Returns:
            dict: All jobs
        """
        return self.tasks.copy()
    
    def run_pending(self):
        """Run pending jobs (call in main loop)"""
        try:
            schedule.run_pending()
        except Exception as e:
            logger.error(f"Error running jobs: {e}")
    
    def start(self):
        """Start scheduler loop"""
        self.is_running = True
        logger.info("Scheduler started")
        
        try:
            while self.is_running:
                self.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Scheduler stopped")
            self.is_running = False
    
    def stop(self):
        """Stop scheduler"""
        self.is_running = False
        logger.info("Scheduler stop requested")


def main():
    """Main entry point"""
    scheduler = TaskScheduler()
    
    # Example job
    def example_task():
        logger.info("Example task executed")
    
    # Add job
    scheduler.add_job(
        "example_job",
        example_task,
        interval=5,
        unit="seconds"
    )
    
    logger.info("Starting scheduler...")
    scheduler.start()


if __name__ == "__main__":
    main()
