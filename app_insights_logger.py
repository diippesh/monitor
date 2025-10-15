# app_insights_logger.py
import logging
import time
import os
from azure.monitor.opentelemetry import configure_azure_monitor

# Step 1: Configure Azure Monitor connection (reads from env variable)
try:
    # Only configure if connection string is available
    if os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"):
        configure_azure_monitor()
        print("Azure Monitor configured successfully")
    else:
        print("Azure Monitor not configured - connection string not found")
except Exception as e:
    print(f"Failed to configure Azure Monitor: {e}")

# Step 2: Set up logger
logger = logging.getLogger("app_insights_custom_logger")
logger.setLevel(logging.INFO)

# Step 3: Send custom log messages
logger.info("🚀 Application Insights custom logging started!")

for i in range(5):
    logger.warning(f"⚠️ Test log {i+1}: Something interesting happened.")
    time.sleep(1)

logger.error("❌ Example error log for testing tracing.")
logger.info("✅ Finished sending custom telemetry logs to Application Insights.")
