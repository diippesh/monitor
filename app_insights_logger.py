# app_insights_logger.py
import logging
import time
import os

# Step 1: Configure Azure Monitor connection (reads from env variable)
def configure_monitoring():
    """Configure Azure Monitor if connection string is available"""
    try:
        # Only configure if connection string is available
        if os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"):
            from azure.monitor.opentelemetry import configure_azure_monitor
            configure_azure_monitor()
            print("Azure Monitor configured successfully")
            return True
        else:
            print("Azure Monitor not configured - connection string not found")
            return False
    except Exception as e:
        print(f"Failed to configure Azure Monitor: {e}")
        return False

# Initialize monitoring
monitoring_enabled = configure_monitoring()

# Step 2: Set up logger
logger = logging.getLogger("app_insights_custom_logger")
logger.setLevel(logging.INFO)

# Step 3: Send custom log messages (only if monitoring is enabled)
if monitoring_enabled:
    logger.info("🚀 Application Insights custom logging started!")
    
    for i in range(5):
        logger.warning(f"⚠️ Test log {i+1}: Something interesting happened.")
        time.sleep(1)
    
    logger.error("❌ Example error log for testing tracing.")
    logger.info("✅ Finished sending custom telemetry logs to Application Insights.")
else:
    print("Skipping telemetry logs - Azure Monitor not configured")
