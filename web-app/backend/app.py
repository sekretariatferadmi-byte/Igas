#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IGAS Web Application API
FastAPI server untuk IGAS
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from loguru import logger
import os
from datetime import datetime

app = FastAPI(
    title="IGAS API",
    description="Integrated Automation & Scraping Tools",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "IGAS API",
        "version": "1.0.0",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health")
async def health():
    """Health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/api/v1/instagram/status")
async def instagram_status():
    """Check Instagram tools status"""
    return {
        "module": "instagram_tools",
        "status": "available",
        "features": [
            "auto_poster",
            "bot",
            "reporter"
        ]
    }


@app.get("/api/v1/bot/status")
async def bot_status():
    """Check Bot status"""
    return {
        "module": "termux_bot",
        "status": "available",
        "features": [
            "system_monitor",
            "task_scheduler"
        ]
    }


@app.get("/api/v1/system/info")
async def system_info():
    """Get system information"""
    try:
        from termux_bot import SystemMonitor
        monitor = SystemMonitor()
        return monitor.get_full_report()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/docs")
async def documentation():
    """API documentation"""
    return {
        "docs_url": "/docs",
        "swagger_ui": "/docs",
        "openapi_schema": "/openapi.json"
    }


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Global exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error", "error": str(exc)}
    )


if __name__ == "__main__":
    import uvicorn
    
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 5000))
    
    logger.info(f"Starting IGAS API on {host}:{port}")
    
    uvicorn.run(
        app,
        host=host,
        port=port,
        reload=os.getenv("API_DEBUG", "true").lower() == "true"
    )
